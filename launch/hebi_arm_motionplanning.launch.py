import os
import yaml

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory

def load_yaml(package_name, file_path):
    pkg_share = get_package_share_directory(package_name)
    yaml_path = os.path.join(pkg_share, file_path)
    with open(yaml_path, 'r') as file:
        return yaml.safe_load(file)

def generate_launch_description():
    hebi_description_pkg = get_package_share_directory('hebi_description')
    hebi_moveit_config_pkg = get_package_share_directory('hebi_a-2240-05_moveit_config')
    
    robot_description = {
        "robot_description": Command([
            FindExecutable(name='xacro'),
            " ",
            PathJoinSubstitution([
                FindPackageShare('hebi_description'),
                "urdf/kits/A-2240-05.urdf.xacro"
            ])
        ])
    }

    srdf_file = os.path.join(hebi_moveit_config_pkg, "config/A-2240-05.srdf")
    with open(srdf_file, 'r') as f:
        robot_description_semantic = {
            "robot_description_semantic": f.read()
        }

    kinematics_yaml = load_yaml("hebi_a-2240-05_moveit_config", "config/kinematics.yaml")
    robot_description_kinematics = {
        "robot_description_kinematics": kinematics_yaml
    }

    planner_plugins_param = {
        "ompl.planning_plugins": ["ompl_interface/OMPLPlanner"]
    }

    use_sim_time_param = {"use_sim_time": True}

    return LaunchDescription([
        Node(
            package='hebi_arm_okblab',
            executable='hebi_arm_motionplanning_node',
            name='hebi_arm_motionplanning_node',
            output='screen',
            parameters=[
                robot_description,
                robot_description_semantic,
                robot_description_kinematics,
                planner_plugins_param,
                use_sim_time_param
            ]
        )
    ])