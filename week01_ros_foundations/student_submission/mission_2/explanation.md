# Mission 2

## Predictions

{'straight': "I predict the robot will finish ahead of it's starting point in a straight path.", 'rotation': 'I predict its position will be rotated counter clockwise, while its direction will  aim towards the left.', 'curve': 'I predict it will go into a forward right motion because the forward speed is 0.15m/s and the turning speed is -0.40 rad/s.', 'curve_modified': 'This path will differ from the first curved trial because the curve will be tighter with the faster speed and faster turning speed.'}

## Prediction Locks

{'straight': '2026-09-06T22:15:06.068141+00:00', 'rotation': '2026-09-06T22:18:29.793857+00:00', 'curve': '2026-09-06T22:26:51.524201+00:00', 'curve_modified': '2026-09-06T22:28:55.992119+00:00'}

## Motion Comparison

For the straight motion trial, the measured motion was captured correctly with my prediction. Since the turning speed is 0 and the forward speed is 0.15m/s, the robot will only move forward. 

## Measurement Explanation

For the first curved trial, the estimated traveled path and start-to-end distance describe different measurements because the turning speed creates a curved path where the robot travels a longer distance than the straight-line distance between its starting and ending positions. Instead of decreasing its traveled path, turning changes the robot’s direction, so it can travel a longer route while ending up closer to where it started.

## Safety Explanation

The command guard checks if the proposed speeds the robot received are possible and can be executed. The final zero command makes sure the robot does not proceed any further with unwanted motion by having a final command that ensures 0 movement. The timeout is needed if the program crashes or communication stops while the robot is moving, ensuring the robot stops after 0.5 seconds if no new command is recieved. 

## Modified Settings

{'linear_x': 0.22, 'angular_z': -0.8, 'duration': 4.0}
