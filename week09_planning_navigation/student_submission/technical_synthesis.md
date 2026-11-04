Across all three missions, I learned that a suitable route for a robot sharing space with people must be efficient, safe, reliable, and practical to execute. Finding the shortest path alone does not guarantee successful navigation.

In Mission 1, BFS and A* both found a 13.5 m path on the open map, but A* expanded only 700 nodes compared to BFS's 928. This showed that heuristics can improve search efficiency while maintaining optimal path length.

In Mission 2, A* successfully navigated the constrained map in 89.5 seconds, while DFS experienced a controller failure after 146.4 seconds. Nav2 completed both maps successfully, requiring 36.0 seconds on the open map and 73.1 seconds on the constrained map. These results demonstrated that route quality and controller performance affect whether a robot can reach its destination.

Mission 3 showed the importance of personal space. A* with social_2 increased minimum person clearance from 0.706 m to 0.809 m while reducing personal space exposure from 1.9 seconds to zero. RRT with social_2 achieved 1.738 m clearance, but RRT with social_1 experienced a controller failure. This demonstrated that stronger social preferences do not always improve navigation.

Finally, these measurements relied on AMCL estimated positions, odometry, and simulated sensor data rather than ground truth robot positions. Therefore, the results demonstrate performance within the simulation but do not guarantee identical behavior in real environments with moving pedestrians.