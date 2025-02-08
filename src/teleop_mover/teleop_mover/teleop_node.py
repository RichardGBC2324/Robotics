import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import subprocess
import os
import signal

class TeleopMover(Node):
    def __init__(self):
        super().__init__('teleop_mover')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info('Starting teleop_twist_keyboard...')
        
        # Launch teleop_twist_keyboard as a subprocess
        self.process = subprocess.Popen(["ros2", "run", "teleop_twist_keyboard", "teleop_twist_keyboard"])
    
    def stop(self):
        self.get_logger().info('Stopping teleop_twist_keyboard...')
        if self.process:
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)  # Kill entire process group
            self.process.wait()  # Wait for process to exit
            self.process = None

def main(args=None):
    rclpy.init(args=args)
    node = TeleopMover()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Keyboard Interrupt received. Shutting down cleanly.")
    finally:
        node.stop()
        node.destroy_node()
        if rclpy.ok():  
            rclpy.shutdown()

if __name__ == '__main__':
    main()
