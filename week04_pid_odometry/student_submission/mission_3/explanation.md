# mission_3 Submission

- Name: Mahbub Ali
- Section: CSCI 39536

## Explanations

### technical_analysis

My prediction was that higher speed or too little derivative control would increase tracking error. The robot computes a heading command from the direction to the next route point. The PID controller adjusts the steering to reduce the heading error and keep the robot on the route. An inaccurate wheel radius causes the robot to estimate its movement incorrectly, so even a well-tuned controller can follow the wrong physical path.

### human_centered_analysis

The most consequential failure is the robot getting too close to or hitting a pedestrian. I would require a larger clearance even if it means using a lower speed. The engineers and safety team are responsible for verifying the decision through testing before the robot is deployed.