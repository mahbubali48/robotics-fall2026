# Lab 7 saved answers

## mission_1.diagnosis
I compared normal_1 and dim_1 using the saved detector settings. In normal_1, the detector selected a box containing the mug, although it also included part of the wooden desk and shadow. The mask showed that the mug and nearby desk had similar HSV values. Contour 4 was selected because it had the largest eligible area (15,292 pixels).

For the dim condition, both cup present images produced detections, but neither bounding box matched the annotated mug at IoU ≥ 0.50. The reduced lighting changed which pixels passed the fixed HSV thresholds, causing inaccurate localization. The value range of 25–150 could not reliably separate the mug from its surroundings under different lighting conditions.

## mission_1.limitations
During practice, I changed the maximum HSV value from 180 to 150 while keeping the other settings the same. This excluded some brighter pixels from the mask and reduced the selected contour area from 17,577 to 15,292 pixels. The resulting bounding box was tighter around the mug, although it still included some of the wooden desk and shadow.

A limitation of this detector is that it relies on fixed color thresholds rather than recognizing objects. A mug with a different color or a background with similar HSV values could cause it to miss the mug or select the wrong region.

## mission_2.choice
I recommend the classical detector for further testing using HSV thresholds of H 0–35, S 70–255, V 25–150, a morphology kernel of 3, minimum area of 300 pixels, and minimum circularity of 0.00. At the learned detector's 0.50 acceptance threshold, the classical method located more mugs in the normal and occluded conditions. Its batch processing time averaged approximately 3.57 ms per image, although processing time alone does not establish robot response speed or safety.

For the normal_1 foreground segmentation example, the mask IoU was 0.5756 and Dice was 0.7306. The predicted foreground included some unwanted regions and missed some mug pixels. A detailed foreground mask does not identify the requested mug because the model does not assign object labels. One limitation of this small test is that its 31 images cannot establish reliable performance across different real-world environments, viewpoints, lighting conditions, or mug appearances.

## mission_2.comparison
I compared the classical and learned detectors on normal, dim, and occluded images. Under normal conditions, the classical detector produced 2 correct boxes, 0 false boxes, and 0 missed mugs, while the learned detector produced 1 correct box, 0 false boxes, and 1 missed mug. Under dim lighting, the classical detector had 0 correct boxes, 2 false boxes, and 2 missed mugs. The learned detector had 0 correct boxes, 0 false boxes, and 2 missed mugs. For occluded images, the classical detector produced 1 correct box, 1 false box, and 1 missed mug, while the learned detector produced 0 correct boxes, 0 false boxes, and 2 missed mugs.

The classical detector located more mugs under these conditions, although it sometimes produced incorrect boxes. For normal_1, the classical detector selected a box covering the mug and some surrounding desk, while the learned detector did not produce an accepted box at the 0.50 threshold. This shows that detecting an object and locating it correctly are different tasks.

## pillar_search.diagnosis
In my blue only attempt (20261023T034914-3fd7a4fe), the robot successfully found and centered the blue pillar. The camera showed the blue pillar, and the HSV mask isolated it as a white region. The yellow centroid indicated the pillar's horizontal position relative to the magenta image center.

When the pillar appeared off center, the controller used the normalized horizontal error to determine the turn direction. A pillar to the left produced a left turn, and the robot continued correcting until the pillar was centered. The image error graph showed the error moving toward the allowed tolerance, and the controller completed the sequence in 16.63 simulation seconds.

I kept the steering gain at 1.20 and center tolerance at 0.10, so I did not test a changed controller setting. The default settings were sufficient for this attempt.

## pillar_search.evidence
In my four color attempt (20261023T042253-ce0c0e86), the robot successfully completed the red, green, turquoise, and blue sequence in 19.41 simulation seconds. The recorded outcome was complete, and the visited colors list included all four colors in the correct order. The controller used the camera's HSV color masks and contour centroids to rotate toward each requested pillar, confirm its alignment, and hold the view before advancing.

The recorded mean absolute image error was approximately 0.3575, reflecting the error throughout the attempt, including the search and turning phases. The completed sequence indicates that all four colors satisfied the controller's centering and hold requirements.

However, a centered colored region does not prove object identity because another similarly colored object could produce a similar mask. It also does not establish distance, because horizontal image alignment provides no depth measurement. Additional sensing would be necessary to determine a reliable physical position.

## line_following.comparison
In the straight practice attempt (20261023T043657-cd7abcad), I used GAIN = 0.08 and SPEED = 0.16. The robot's image error initially oscillated around zero but gradually settled, with a mean absolute error of 0.0489. The magenta line was tracked reasonably well on the straight section, although one line loss event occurred.

On the curved track, I compared steering gains of 0.08 and 0.30 while keeping the other settings unchanged. Both attempts reached the finish, but increasing the gain improved the robot's ability to correct its direction around bends. Mean absolute image error decreased from 0.4867 to 0.1739, and simulation time decreased from 187.38 to 137.53 seconds. Neither track attempt recorded a line loss event.

The mask provided the line region, and its centroid determined the steering error. The controller used negative gain times error to turn toward the line. The stronger gain produced larger corrective turns, helping the robot stay closer to the line on the curved route.

## line_following.limits
During my straight practice attempt, the controller recorded one line loss event. The final saved camera image showed a yellow floor region with no visible magenta line, and the mask was black. This indicates that the image processing pipeline could not identify a valid line contour in that frame. The controller entered its safe stopping state rather than continuing forward without reliable line evidence.

For a real delivery robot operating around people, camera-based line following alone would not be sufficient. Additional sensing, such as depth cameras or lidar for obstacle detection, wheel encoders and an IMU for motion estimation, and emergency stopping capabilities would be needed. The robot should also be tested under changing lighting, different floor surfaces, moving pedestrians, unexpected obstacles, and sensor failures before real-world operation.

## final.synthesis
The three missions taught me that reliable robot behavior depends on both accurate visual detection and how the robot responds to that information.

In Mission 1, I compared classical HSV based detection with learned models for locating a mug. My classical detector achieved 75% bounding box precision and recall across 31 images. Although it detected cup presence in every case correctly, some bounding boxes included parts of the wooden desk. The learned detector also struggled under certain conditions, especially dim lighting. This showed me that detecting something in an image does not guarantee locating the correct object.

In Mission 2, I used live camera feedback to center colored pillars. My four color attempt (20261023T042253-ce0c0e86) successfully completed red, green, turquoise, and blue in 19.41 simulation seconds. The robot used HSV masks and contour centroids to calculate horizontal error and adjust its turning direction. This demonstrated how camera measurements can guide robot movement through repeated corrections.

In Mission 3, I compared two line following controllers on the curved track. With GAIN = 0.08, the robot completed the route with a mean absolute image error of 0.4867. After increasing the gain to 0.30, the error decreased to 0.1739, and completion time decreased from 187.38 to 137.53 simulation seconds. This suggests that stronger steering corrections helped the robot follow the bends more accurately.

Overall, these experiments showed that perception and control must work together. Changing a color threshold or steering gain can significantly affect the outcome. However, limitations remain because color based vision can confuse similar objects, camera alignment does not measure distance, and performance in a small simulation does not guarantee safety around people. A real robot would need additional sensing, obstacle detection, and extensive testing under different environmental conditions.

## final.course_reflection
I enjoyed this lab because it was very interactive and gave me the opportunity to see how computer vision and robotics work together in practice. Instead of just reading about image processing and control systems, I could adjust parameters, run experiments, and immediately observe how those changes affected the robot's behavior. Watching the robot locate colored pillars and follow a line made the concepts more interesting and easier to understand.

This activity positively affected my motivation to explore more work involving robotics, programming, and computer vision. I especially liked seeing how small changes, such as adjusting the steering gain, could make a noticeable difference in the robot's performance.

One important takeaway was the role of safety, reliability, and human centered design. A robot might successfully detect an object or complete a route in simulation, but that does not necessarily mean it would operate safely around people. This showed me why engineers need to consider real world conditions, unexpected situations, and human safety alongside technical performance.

One frustrating part of the experience was how the lab occasionally derailed because of technical issues with Docker, ROS, Gazebo, and the virtual desktop. I spent a significant amount of time troubleshooting the environment instead of focusing on the actual activities. However, working through those problems also taught me the importance of patience, troubleshooting, and understanding the tools I'm using.

Overall, despite the technical difficulties, I found the lab engaging and rewarding. It made me more interested in continuing to learn about robotics and building systems that are both functional and reliable.
