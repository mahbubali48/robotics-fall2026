# Mission 3

## Data To Command

The first function finds the nearest valid LiDAR distance ahead of the robot. The second function uses that distance to decide whether the robot should move forward or stop.


## Missing Data Safety

The robot stops because without a valid front measurement, it cannot tell if there is an obstacle ahead. Treating the path as clear could cause the robot to crash.


## System Layers

My decision functions determine the speed based on the LiDAR readings. The supplied ROS node sends that proposed speed to "/student_cmd_vel", and the command guard checks it before sending the approved command to "/cmd_vel".

