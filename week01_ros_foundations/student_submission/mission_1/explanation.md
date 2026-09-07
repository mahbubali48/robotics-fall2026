# Mission 1

## Scan Observation

I found the range min and range max, which represents the minimum and maximum distances recorded around the robot.

## Guided Checks

{'node_list': True, 'guard_info': True, 'bridge_info': True, 'scan_info': True, 'scan_message': True, 'command_topics': True}

## Graph Explanation

A ROS 2 graph shows the programs running in the robot system and how they communicate with each other. For example, the /ros_gz_bridge node publishes sensor data on the /scan topic.

## Command Path Explanation

A proposed command travels on /student_cmd_vel. This guard checks whether the command is safe, then sends the approved command on /cmd_vel so the robot can move.

## Tools Explanation

Gazebo is responsible for simulating the robot, its movement, sensors, and environment, while RViz is responsible for displaying ROS 2 data so you can see what the robot is sensing and doing.
