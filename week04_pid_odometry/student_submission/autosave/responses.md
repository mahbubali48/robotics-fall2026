# Autosaved responses

- Name: Mahbub Ali
- Student ID: mahbub.ali86@login.cuny.edu
- Section: CSCI 39536

## Check-in answers

### background_compare

A human engineer chooses the PID gains (Kp, Ki, and Kd) based on how they want the system to respond. They decide how quickly the system should reach its target, how much overshoot is acceptable, and how stable the response should be. PID is a feedback controller because it continuously measures the system's current state, compares it to the desired state, calculates the error, and uses that error to adjust the command.

### background_social

A car's braking system is an example of a system controlled by feedback. If the controller is tuned too aggressively, the brakes could respond too strongly and cause sudden or unstable braking, which could put passengers or nearby drivers at risk. If it is tuned too cautiously, the brakes may respond too slowly, increasing the stopping distance and potentially causing the car to stop too late.

### pid_playground_terms

The P term reacted first because it responds immediately to the current error. The I term eliminated the final gap because it builds up error over time and keeps correcting until the target is reached.

### odom_background_wheels

The robot turns left. Using the heading formula, change in heading equals (right wheel distance - left wheel distance) divided by the track width. Since the right wheel moves 6 cm and the left wheel moves 0 cm, the change in heading is positive, so the robot turns left.

### m1_prediction

With too little Kp, I expect the arm to move slowly and struggle to reach or hold the target. With too little Kd, I expect the arm to overshoot the target and oscillate before settling.

### m1_arm_tuning

I predicted that low Kp would make the arm weak or slow and low Kd would cause overshoot. I increased Kp and Kd on the shoulder and elbow to improve the response. The hold phase showed less error and less oscillation. Gravity compensation helped the arm resist gravity and hold the target more accurately.

### m2_prediction

The estimated forward distance will be too large because the forward pod scale is too large, while the estimated sideways distance will be too small because the strafe pod scale is too small.

### m2_analysis

My prediction matched the test. The forward scale changed how much forward distance was estimated, while the sideways scale changed the estimated sideways distance. The sideways pod is needed because the robot can move sideways and the forward pod cannot measure that motion. Some drift can remain because small measurement errors build up as the robot moves.

### m3_prediction

Increasing speed may increase tracking error because the robot has less time to correct its path. Too little derivative control may cause overshoot and oscillation when turning. Therefore, both can reduce pedestrian clearance and make the route less safe.

### m3_technical

My prediction was that higher speed or too little derivative control would increase tracking error. The robot computes a heading command from the direction to the next route point. The PID controller adjusts the steering to reduce the heading error and keep the robot on the route. An inaccurate wheel radius causes the robot to estimate its movement incorrectly, so even a well-tuned controller can follow the wrong physical path.

### m3_human

The most consequential failure is the robot getting too close to or hitting a pedestrian. I would require a larger clearance even if it means using a lower speed. The engineers and safety team are responsible for verifying the decision through testing before the robot is deployed.

### final_reflection

I really liked the trial-and-error style of this lab. Being able to adjust different values, see the resulting error, and keep making changes until the robot followed the ideal path as closely as possible made the concepts much easier to understand. This activity positively affected my motivation to do similar work in the future because I enjoyed seeing the direct results of the changes I made. The lab also showed me the importance of safety and being meticulous when working with robotics. Small changes in controller settings, speed, or calibration can affect how a robot behaves around people, so technical performance and safety have to be considered together. What stood out most to me was how interactive the lab was. I liked that I could focus directly on experimenting with PID control, odometry, and navigation without having to enter a virtual lab environment and work through ROS, which can sometimes feel clunky to use. This was probably my favorite lab so far because it was quick, concise, and hands on. The initial setup took a while, especially because I needed to install the correct Python version, but once everything was running, the actual lab was straightforward and fun.

## Mission explanations

### mission_1

**prediction**: With too little Kp, I expect the arm to move slowly and struggle to reach or hold the target. With too little Kd, I expect the arm to overshoot the target and oscillate before settling.

**tuning_analysis**: I predicted that low Kp would make the arm weak or slow and low Kd would cause overshoot. I increased Kp and Kd on the shoulder and elbow to improve the response. The hold phase showed less error and less oscillation. Gravity compensation helped the arm resist gravity and hold the target more accurately.

### mission_2

**prediction**: The estimated forward distance will be too large because the forward pod scale is too large, while the estimated sideways distance will be too small because the strafe pod scale is too small.

**calibration_analysis**: My prediction matched the test. The forward scale changed how much forward distance was estimated, while the sideways scale changed the estimated sideways distance. The sideways pod is needed because the robot can move sideways and the forward pod cannot measure that motion. Some drift can remain because small measurement errors build up as the robot moves.

### mission_3

**technical_analysis**: My prediction was that higher speed or too little derivative control would increase tracking error. The robot computes a heading command from the direction to the next route point. The PID controller adjusts the steering to reduce the heading error and keep the robot on the route. An inaccurate wheel radius causes the robot to estimate its movement incorrectly, so even a well-tuned controller can follow the wrong physical path.

**human_centered_analysis**: The most consequential failure is the robot getting too close to or hitting a pedestrian. I would require a larger clearance even if it means using a lower speed. The engineers and safety team are responsible for verifying the decision through testing before the robot is deployed.
