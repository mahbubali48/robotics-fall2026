# line_following

## comparison
In the straight practice attempt (20261023T043657-cd7abcad), I used GAIN = 0.08 and SPEED = 0.16. The robot's image error initially oscillated around zero but gradually settled, with a mean absolute error of 0.0489. The magenta line was tracked reasonably well on the straight section, although one line loss event occurred.

On the curved track, I compared steering gains of 0.08 and 0.30 while keeping the other settings unchanged. Both attempts reached the finish, but increasing the gain improved the robot's ability to correct its direction around bends. Mean absolute image error decreased from 0.4867 to 0.1739, and simulation time decreased from 187.38 to 137.53 seconds. Neither track attempt recorded a line loss event.

The mask provided the line region, and its centroid determined the steering error. The controller used negative gain times error to turn toward the line. The stronger gain produced larger corrective turns, helping the robot stay closer to the line on the curved route.

## limits
During my straight practice attempt, the controller recorded one line loss event. The final saved camera image showed a yellow floor region with no visible magenta line, and the mask was black. This indicates that the image processing pipeline could not identify a valid line contour in that frame. The controller entered its safe stopping state rather than continuing forward without reliable line evidence.

For a real delivery robot operating around people, camera-based line following alone would not be sufficient. Additional sensing, such as depth cameras or lidar for obstacle detection, wheel encoders and an IMU for motion estimation, and emergency stopping capabilities would be needed. The robot should also be tested under changing lighting, different floor surfaces, moving pedestrians, unexpected obstacles, and sensor failures before real-world operation.
