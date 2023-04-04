import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

# Main launch script for starting simulation with my robots
def generate_launch_description():

    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # YOO MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='turtlebot3_waffle_pi' #<--- CHANGE ME WHEN USING DIFFERENT PACKAGE

    # This Launch file handles the simulation of the environment (Gazebo)
    start_world = IncludeLaunchDescription(
                    PythonLaunchDescriptionSource([os.path.join(
                        get_package_share_directory(package_name),'launch','start_world.launch.py')]),
    )

    # This launch file handles the simulation of the robots
    start_robots = IncludeLaunchDescription(
                            PythonLaunchDescriptionSource(os.path.join(
                                get_package_share_directory(package_name),'launch','start_robots.launch.py')),
    )     

    # Launch them all!
    return LaunchDescription([
        #rsp,
        #start_robots,
        start_world
        #spawn_entity,
        #gazebo
    ])