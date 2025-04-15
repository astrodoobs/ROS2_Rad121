from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    param_file = os.path.join(
        get_package_share_directory('rad121_monitor'),
        'params',
        'heatmap.yaml'
    )

    return LaunchDescription([
        Node(
            package='rad121_monitor',
            executable='rad_heatmap_node',
            name='rad_heatmap_node',
            parameters=[{'use_sim_time': True},param_file],
            output='screen'
        )
    ])
