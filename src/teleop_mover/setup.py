from setuptools import find_packages, setup

package_name = 'teleop_mover'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rxpweji',
    maintainer_email='rxpweji@todo.todo',
    description='A simple ROS 2 teleop node that runs teleop_twist_keyboard',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
	'teleop_node = teleop_mover.teleop_node:main',
        ],
    },
)
