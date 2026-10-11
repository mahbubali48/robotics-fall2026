# Week 6: SLAM and Mapping

- name: Mahbub Ali
- email: mahbub.ali86@login.cuny.edu

## final.course_reflection

This lab was honestly one of the more frustrating experiences I've had in robotics so far. I understand the importance of SLAM, LiDAR, and occupancy grid mapping, but the browser based simulation environment made the activity much more difficult than I expected. The software was slow, the controls felt clunky, and there was noticeable input delay when trying to navigate the robot. Even simple movements required a lot of effort, especially when the robot behaved unpredictably near walls and tight spaces.

This experience affected my motivation negatively toward robotics because it made me question whether this is how robotics development is normally done. If it is, I find that discouraging. However, it also made me interested in finding better, faster, and more responsive software tools that make robotics development more efficient and enjoyable.

One important takeaway was understanding the value of efficient occupancy grid mapping. Accurate maps are essential for reliable navigation, especially when robots operate in environments shared with people. Efficient mapping can help robots navigate safely, avoid obstacles, and perform useful tasks in real world applications.

What stood out most was how much time was spent dealing with software responsiveness and navigation difficulties rather than focusing on the actual mapping concepts. I'm not sure whether the performance issues were caused by my hardware, the browser based environment, or the simulation itself, but they made the lab significantly harder to complete.

Overall, this was not my favorite lab. Although I learned more about SLAM and mapping, I believe the experience would have been much more productive with a smoother and more responsive simulation environment.

## final.synthesis

During Lab 6, I explored how SLAM combines robot motion estimates with LiDAR measurements to construct an occupancy grid map. Odometry provides an estimate of the robot's movement, but accumulated errors can affect its estimated position over time. LiDAR measures distances to surrounding objects, allowing SLAM to identify walls, obstacles, and free space. By combining these observations, SLAM updates the robot's estimated pose and progressively builds a map that distinguishes occupied, free, and unknown areas.

In Mission 1, I used a limited exploration strategy and recorded 30 minutes, while Mission 2 used a corridor first strategy and recorded 10 minutes. Both runs produced saved occupancy grid maps, although controlling the TurtleBot3 was challenging. The robot behaved unpredictably near walls and tight spaces and eventually tipped over during Mission 2. These difficulties limited the amount of space I could explore and highlighted how robot movement, sensor visibility, and exploration strategy affect mapping results. The input delay and slow simulation performance also made precise navigation difficult.

The experiment demonstrated that producing a useful map requires more than simply moving the robot. Reliable motion, sufficient LiDAR coverage, and revisiting recognizable areas can help improve map consistency. Unknown regions can remain when walls or furniture obstruct the LiDAR's line of sight or when the robot cannot reach certain locations. Revisiting previously mapped areas may help SLAM correct accumulated positioning errors, although I could not clearly verify loop closure during my exploration.

Overall, this lab helped me understand how motion estimation, sensor observations, and exploration strategies work together. I learned that faster mapping does not necessarily produce a better map, especially when navigation difficulties prevent sufficient environmental coverage.

## mission_1.drift_and_revisit

During my exploration, I attempted to navigate through the house, but the TurtleBot3 was difficult to control and sometimes moved unpredictably. I could not clearly determine whether new LiDAR scans aligned perfectly with previously mapped walls or whether any walls shifted or appeared doubled. I also could not confirm that SLAM successfully corrected accumulated drift through loop closure. To verify this, I would need clearer RViz observations showing the same wall before and after revisiting it, along with evidence of changes in the robot's estimated pose or map alignment.

## mission_1.limitations

When I stopped mapping, parts of the house remained unknown or poorly outlined, particularly areas beyond the corridors and rooms I was able to explore. My RViz map contained approximately 50% unknown cells. I had difficulty controlling the TurtleBot3 because its movement was unstable and difficult to navigate precisely. Although I managed to get inside the house, I could not explore all the rooms. The LiDAR could only detect surfaces within its range and direct line of sight, so walls, corners, and furniture blocked scans from reaching unexplored areas. As a result, my map was incomplete.

## mission_1.route.original_prediction

I plan to begin near the center left of the house and slowly explore the accessible corridors and rooms using keyboard teleoperation. I will follow walls, pass through accessible doorways, and observe the occupancy grid map in RViz as LiDAR scans reveal the environment. I will explore different sides of obstacles to reduce unknown areas while avoiding collisions. After covering the main accessible spaces, I will return to a recognizable wall or junction to help SLAM detect a previously visited location and potentially correct accumulated mapping errors.

## mission_1.route.prediction_draft

I plan to begin near the center left of the house and slowly explore the accessible corridors and rooms using keyboard teleoperation. I will follow walls, pass through accessible doorways, and observe the occupancy grid map in RViz as LiDAR scans reveal the environment. I will explore different sides of obstacles to reduce unknown areas while avoiding collisions. After covering the main accessible spaces, I will return to a recognizable wall or junction to help SLAM detect a previously visited location and potentially correct accumulated mapping errors.

## mission_2.comparison

In Mission 1, I used a limited exploration strategy and recorded 30 minutes, while in Mission 2, I used a corridor first strategy and recorded 10 minutes. Mission 2 took 20 fewer minutes, representing a 66.7% reduction in recorded exploration time. Both strategies produced saved occupancy grid maps, but controlling the TurtleBot3 was difficult, particularly near walls and narrow spaces. The robot also tipped over during Mission 2, limiting further exploration. Although the second run was faster, comparing map coverage and wall consistency is necessary to determine whether it produced a better map.

## mission_2.map_choice

I would choose the map that provides the most useful representation of the accessible house, rather than selecting one based only on completion time. Mission 1 took longer but involved more time attempting to navigate the environment. Mission 2 was faster using a corridor first approach, but the robot became unstable near obstacles and eventually tipped over. I would compare the known area fraction, unknown area fraction, and consistency of mapped walls before choosing the better result. A shorter exploration time does not necessarily mean the map is more accurate or complete.

## mission_2.strategy.original_prediction

For Mission 2, I plan to use a corridor first exploration strategy instead of the limited exploration approach from Mission 1. I will start from the robot's original position and focus on navigating through the main accessible corridors before attempting to enter individual rooms. I will use slower, more controlled movements and stop frequently to adjust the robot's direction. My goal is to create clearer wall outlines, reduce unknown areas along my route, and avoid the navigation difficulties I experienced during Mission 1. I will compare the resulting map coverage, quality score, and completion time with my first attempt.

## mission_2.strategy.prediction_draft

For Mission 2, I plan to use a corridor first exploration strategy instead of the limited exploration approach from Mission 1. I will start from the robot's original position and focus on navigating through the main accessible corridors before attempting to enter individual rooms. I will use slower, more controlled movements and stop frequently to adjust the robot's direction. My goal is to create clearer wall outlines, reduce unknown areas along my route, and avoid the navigation difficulties I experienced during Mission 1. I will compare the resulting map coverage, quality score, and completion time with my first attempt.
