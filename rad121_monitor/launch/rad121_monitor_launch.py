from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    param_file = os.path.join(
        get_package_share_directory('rad121_monitor'),
        'params',
        'sensor.yaml'
    )

    return LaunchDescription([
        Node(
            package='rad121_monitor',
            executable='rad121_monitor_node',
            name='rad121_monitor_node',
            parameters=[param_file],
            output='screen'
        )
    ])
