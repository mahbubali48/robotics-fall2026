# Mission 3

## Specification

The robot will complete four forward arcs in this order: +45°, -45°, +45°, and -45°, finishing facing its original direction. I will use a linear speed of 0.18 m/s and an angular speed of ±0.60 rad/s, giving a radius of 0.30 m. Each arc will run for about 1.31 seconds. After the final arc, the robot will send a zero velocity command to stop. Success means each arc is within 0.02 m of the 0.30 m radius and within 0.04 rad of the intended 45° turn, while staying within the speed and time limits.

## Saved Specification

The robot will complete four forward arcs in this order: +45°, -45°, +45°, and -45°, finishing facing its original direction. I will use a linear speed of 0.18 m/s and an angular speed of ±0.60 rad/s, giving a radius of 0.30 m. Each arc will run for about 1.31 seconds. After the final arc, the robot will send a zero velocity command to stop. Success means each arc is within 0.02 m of the 0.30 m radius and within 0.04 rad of the intended 45° turn, while staying within the speed and time limits.

## Assigned Pattern

alternating_arcs

## Original Prompt

My specification:
The robot will complete four forward arcs in this order: +45°, -45°, +45°, and -45°, finishing facing its original direction. I will use a linear speed of 0.18 m/s and an angular speed of ±0.60 rad/s, giving a radius of 0.30 m. Each arc will run for about 1.31 seconds. After the final arc, the robot will stop. Success means each arc is within 0.02 m of the 0.30 m radius and within 0.04 rad of the intended 45° turn, while staying within the speed and time limits.

This is a ROS 2 Jazzy Python package. Implement only build_pattern(pattern_name: str) -> list[Segment] for 'alternating_arcs' in the existing pattern.py.
The course-provided pattern_node.py calls this function, publishes the returned segments repeatedly through /student_cmd_vel, and sends the final zero command.
Use the existing Segment class with linear_x (m/s), angular_z (rad/s), and duration (s).
Return the ordered segments for the assigned specification and raise ValueError for an unknown pattern name.
Stay within 0.22 m/s, 0.80 rad/s, 30 seconds per segment, and 60 seconds total.
Do not replace the wrapper or course checks. Explain assumptions and propose tests.

## Original Output

Assumptions: the existing `Segment` class is already defined in `pattern.py`, positive `angular_z` turns left, negative `angular_z` turns right, and the course wrapper handles repeated publishing and the final zero-velocity stop. With `linear_x = 0.18 m/s` and `|angular_z| = 0.60 rad/s`, the arc radius is:

$$
R=\frac{v}{|\omega|}=\frac{0.18}{0.60}=0.30\text{ m}
$$

A 45° turn is \(\pi/4\) radians, so each arc should last:

$$
t=\frac{\pi/4}{0.60}\approx1.309\text{ s}
$$

```python
import math


def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "alternating_arcs":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    duration = (math.pi / 4.0) / 0.60

    return [
        Segment(linear_x=0.18, angular_z=0.60, duration=duration),
        Segment(linear_x=0.18, angular_z=-0.60, duration=duration),
        Segment(linear_x=0.18, angular_z=0.60, duration=duration),
        Segment(linear_x=0.18, angular_z=-0.60, duration=duration),
    ]
```

Tests should verify that there are exactly four segments, the angular directions alternate `+ - + -`, each arc has a radius of approximately `0.30 m`, each segment turns approximately `π/4` radians in magnitude, all speed and duration limits are respected, the total heading change is approximately zero, and an unknown pattern name raises `ValueError`.


## Original Source

import math


def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "alternating_arcs":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    duration = (math.pi / 4.0) / 0.60

    return [
        Segment(linear_x=0.18, angular_z=0.60, duration=duration),
        Segment(linear_x=0.18, angular_z=-0.60, duration=duration),
        Segment(linear_x=0.18, angular_z=0.60, duration=duration),
        Segment(linear_x=0.18, angular_z=-0.60, duration=duration),
    ]

## Assumptions

The AI assumed the robot uses meters, seconds, and radians, with +x as forward and positive angular velocity as a left turn. It assumed constant linear and angular speeds during each segment and no wheel slip or acceleration effects. It also assumed the wrapper handles timing accurately, repeatedly publishes each segment, and sends the final stop command.

## Problems

I did not find a major error in the generated code, but I checked the speed limits, arc radius, 45° turn angle, segment order, total duration, and final heading. One omission is that the AI assumes ideal constantvvelocity motion and does not account for real effects like acceleration, wheel slip, or timing delays. I also verified that the wrapper, not build_pattern, is responsible for repeatedly publishing commands and sending the final stop.

## Test Plan

Pattern behavior test: Check that the function returns four arcs in the order +45°, -45°, +45°, -45°. 
Expected result: four segments with alternating angular velocity signs and a final net heading change of about 0 radians. 
Velocity limit test: Check that every segment stays within 0.22 m/s linear and 0.80 rad/s angular speed. Expected result: all segments pass because they use 0.18 m/s and ±0.60 rad/s. 
Stop test: Verify that the course wrapper sends zero linear and angular velocity after the last segment. 
Expected result: the robot stops completely after the pattern finishes.

## Modifications

I kept the existing Segment class and replaced the NotImplementedError with four alternating arc segments. I used 0.18 m/s linear speed and ±0.60 rad/s angular speed to produce a 0.30 m radius. I calculated each duration from a 45° turn and added a ValueError for unknown patterns. I also used named variables to make the calculations easier to review. The pattern and velocity tests will verify the segment order, radius, turn angles, and speed limits.

## Live Pending

True

## Evidence Analysis

The tests establish that the code structure and planned geometry are correct. All 9 tests passed, the commands stayed within the speed limits, the alternating arc shape check passed, and the model stop check passed. The live run also completed and verified the final stop. However, these tests do not prove that the real/simulated robot follows the expected path closely enough during execution, since shape_observed was false and some checkpoint errors exceeded the live tolerances. One additional condition I would need is a successful live run where every checkpoint stays within the required position and heading tolerances.

## Ai Disclosure

I used ChatGPT to help generate and review the ROS 2 Python code for the camera transform and alternating arcs motion pattern, as well as to suggest tests and explain the motion calculations. I personally checked the frame names, speed limits, arc radius, turn angles, segment order, timing, and stopping behavior. I also changed the final pattern.py to use clearer named variables and added two assignment specific tests. I verified the work by running the course tests, confirming 5/5 camera transform tests and 9/9 motion pattern tests passed, and by completing the live motion run and checking its stop and checkpoint results.

## Live Issue

The first live run failed because Gazebo and the course command guard were not running. I restarted the lab, ran preflight, and confirmed the simulation clock, odometry, command guard, and transforms all passed. I then reran the pattern successfully, and the final stop was verified. However, shape_observed was still false because some live checkpoint position and heading errors exceeded the allowed tolerances. The remaining unverified behavior is whether the robot can reproduce the alternating arc shape within the required live tolerances.
