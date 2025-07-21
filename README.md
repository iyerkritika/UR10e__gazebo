# UR10e gazebo and Rviz simulation

This repository is forked from [Universal_Robots_ROS2_Description](https://github.com/UniversalRobots/Universal_Robots_ROS2_Description). It has been modified to launch Gazebo as well as Rviz for only the UR10e. I have also added a prismaticc joint at the base of the UR10e.

The instructions are for executing on ROS2 Humble with ignition Gazebo. Please make sure you have them installed.

## Structure of the repository

The most relevant files are:
  - `urdf/ur_macro.xacro` - macro file with UR-manipulator description. This file is usually included into external projects to visualize and configure UR manipulators properly. An example how to use this macro is in `urdf/ur.urdf.xacro` file.
  - `urdf/ur.ros2_control.xacro` - definition of manipulator's joints and interfaces for `ros2_control` framework.

## Testing description of a manipulator

To visualize the robot install this repository to you workspace by executing:

``` bash
cd <path_to_repo>
colcon build --symlink-install
source <path_to_repo>install/setup.bash 
export IGN_GAZEBO_RESOURCE_PATH=<path_to_repo>/install/ur_description/share/
```
After that please execute :
```bash
ros2 launch ur_description view_ur.launch.py ur_type:=ur10e
```

I have also created a *tf_gen.py* file that calculates the FK given the dh parameters. Through this I have calculated the IK as well. 

I have not been able to decouple a lot of the angles through IK yet. 


