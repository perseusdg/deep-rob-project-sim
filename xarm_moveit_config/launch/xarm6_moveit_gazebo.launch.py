#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    hw_ns = LaunchConfiguration('hw_ns', default='xarm')
    
    # robot moveit gazebo launch
    robot_moveit_gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('xarm_moveit_config'), 'launch', '_robot_moveit_gazebo.launch.py'])),
        launch_arguments={
            'dof': '6',
            'robot_type': 'xarm',
            'hw_ns': hw_ns,
            'no_gui_ctrl': 'false',
            'add_realsense_d435i': 'true',
            'add_gripper': 'true',
            'attach_to': 'world',
            'attach_xyz': '-0.4 0.5 0.0',  # Move to other side: +X forward, -Y across table
            'attach_rpy': '0.0 0.0 1.5',  # Rotate 180 degrees around Z axis (in radians)
            'realsense_attach_to': 'world',
            'realsense_attach_xyz': '0 0 1.5',
            'realsense_attach_rpy': '0 0 0'
        }.items(),
    )
    
    return LaunchDescription([
        robot_moveit_gazebo_launch
    ])