# mission_2 Submission

- Name: Mahbub Ali
- Section: CSCI 39536

## Explanations

### prediction

The estimated forward distance will be too large because the forward pod scale is too large, while the estimated sideways distance will be too small because the strafe pod scale is too small.

### calibration_analysis

My prediction matched the test. The forward scale changed how much forward distance was estimated, while the sideways scale changed the estimated sideways distance. The sideways pod is needed because the robot can move sideways and the forward pod cannot measure that motion. Some drift can remain because small measurement errors build up as the robot moves.