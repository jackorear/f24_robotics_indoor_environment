from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='webots_ros2_driver',
            executable='webots_launcher',
            output='screen',
            arguments=['--world', 'worlds/NERC_basement.wbt']
        ),
    ])