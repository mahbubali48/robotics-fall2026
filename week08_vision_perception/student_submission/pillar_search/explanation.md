# pillar_search

## diagnosis
In my blue only attempt (20261023T034914-3fd7a4fe), the robot successfully found and centered the blue pillar. The camera showed the blue pillar, and the HSV mask isolated it as a white region. The yellow centroid indicated the pillar's horizontal position relative to the magenta image center.

When the pillar appeared off center, the controller used the normalized horizontal error to determine the turn direction. A pillar to the left produced a left turn, and the robot continued correcting until the pillar was centered. The image error graph showed the error moving toward the allowed tolerance, and the controller completed the sequence in 16.63 simulation seconds.

I kept the steering gain at 1.20 and center tolerance at 0.10, so I did not test a changed controller setting. The default settings were sufficient for this attempt.

## evidence
In my four color attempt (20261023T042253-ce0c0e86), the robot successfully completed the red, green, turquoise, and blue sequence in 19.41 simulation seconds. The recorded outcome was complete, and the visited colors list included all four colors in the correct order. The controller used the camera's HSV color masks and contour centroids to rotate toward each requested pillar, confirm its alignment, and hold the view before advancing.

The recorded mean absolute image error was approximately 0.3575, reflecting the error throughout the attempt, including the search and turning phases. The completed sequence indicates that all four colors satisfied the controller's centering and hold requirements.

However, a centered colored region does not prove object identity because another similarly colored object could produce a similar mask. It also does not establish distance, because horizontal image alignment provides no depth measurement. Additional sensing would be necessary to determine a reliable physical position.
