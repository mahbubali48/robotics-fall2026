# Mission 1

## Drift And Revisit

During my exploration, I attempted to navigate through the house, but the TurtleBot3 was difficult to control and sometimes moved unpredictably. I could not clearly determine whether new LiDAR scans aligned perfectly with previously mapped walls or whether any walls shifted or appeared doubled. I also could not confirm that SLAM successfully corrected accumulated drift through loop closure. To verify this, I would need clearer RViz observations showing the same wall before and after revisiting it, along with evidence of changes in the robot's estimated pose or map alignment.

## Limitations

When I stopped mapping, parts of the house remained unknown or poorly outlined, particularly areas beyond the corridors and rooms I was able to explore. My RViz map contained approximately 50% unknown cells. I had difficulty controlling the TurtleBot3 because its movement was unstable and difficult to navigate precisely. Although I managed to get inside the house, I could not explore all the rooms. The LiDAR could only detect surfaces within its range and direct line of sight, so walls, corners, and furniture blocked scans from reaching unexplored areas. As a result, my map was incomplete.

## Route.Original Prediction

I plan to begin near the center left of the house and slowly explore the accessible corridors and rooms using keyboard teleoperation. I will follow walls, pass through accessible doorways, and observe the occupancy grid map in RViz as LiDAR scans reveal the environment. I will explore different sides of obstacles to reduce unknown areas while avoiding collisions. After covering the main accessible spaces, I will return to a recognizable wall or junction to help SLAM detect a previously visited location and potentially correct accumulated mapping errors.

## Route.Prediction Draft

I plan to begin near the center left of the house and slowly explore the accessible corridors and rooms using keyboard teleoperation. I will follow walls, pass through accessible doorways, and observe the occupancy grid map in RViz as LiDAR scans reveal the environment. I will explore different sides of obstacles to reduce unknown areas while avoiding collisions. After covering the main accessible spaces, I will return to a recognizable wall or junction to help SLAM detect a previously visited location and potentially correct accumulated mapping errors.
