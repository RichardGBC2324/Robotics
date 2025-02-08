from setuptools import setup

package_name = 'teleop_mover'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='A simple ROS 2 teleop node that runs teleop_twist_keyboard',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_node = teleop_mover.teleop_node:main',
        ],
    },
)
