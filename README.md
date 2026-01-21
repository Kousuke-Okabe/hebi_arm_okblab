# 環境構築
1. HEBI C+; API
    > sudo apt-get install ros-$ROS_DISTRO-hebi-cpp-api
2. hebi_bringup
    > git clone -b $ROS_DISTRO https://github.com/HebiRobotics/hebi_bringup.git
3. hebi_description
    > git clone -b ros2/$ROS_DISTRO https://github.com/HebiRobotics/hebi_description.git # ROS_DISTRO can be either humble, iron, or jazzy

4. hebi_hardware
    > git clone -b $ROS_DISTRO https://github.com/HebiRobotics/hebi_hardware.git
5. hebi_moveit_config
    > git clone https://github.com/HebiRobotics/hebi_moveit_configs.git
6. hebi_msgs
    > git clone https://github.com/HebiRobotics/hebi_msgs.git


# 実行

### 実機動作
tarminal 1
> ros2 launch hebi_bringup bringup_arm.launch.py hebi_arm:="A-2240-05" use_mock_hardware:=false use_rviz:=false

terminal 2
> ros2 launch hebi_bringup move_group.launch.py hebi_arm:="A-2240-05" use_sim_time:=false

terminal 3
> ros2 launch hebi_arm_okblab hebi_arm_motionplanning.launch.py

### シミュレーション動作
tarminal 1
> ros2 launch hebi_bringup bringup_arm_gazebo.launch.py hebi_arm:="A-2240-05" use_mock_hardware:=false use_rviz:=false

terminal 2
> ros2 launch hebi_bringup move_group.launch.py hebi_arm:="A-2240-05" use_sim_time:=true

terminal 3
> ros2 launch hebi_arm_okblab hebi_arm_motionplanning.launch.py