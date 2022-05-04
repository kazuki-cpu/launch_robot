from glob import glob
from setuptools import setup

package_name = 'launch_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kazuki-cpu',
    maintainer_email='Kazuki-Fujiwara@outlook.com',
    description='Test launch program for raspberry pi robot',
    license=' Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_manager = py_robot.robot.manager:main',
            'status_manager = py_robot.status_publisher:main',
            'pwm_listener = py_robot.pwm_subscriber:main',
        ],
    },
)
