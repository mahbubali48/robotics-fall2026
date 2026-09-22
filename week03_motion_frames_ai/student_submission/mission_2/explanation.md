# Mission 2

## Frame Context

The rear camera is physically attached to the robot, so its position and orientation relative to base_link stay constant as the robot moves. The hallway camera is fixed in the environment, while base_link moves with the robot. SInce the robot changes position and orientation relative to the fixed hallway camera, the hall_camera to base_link transform changes over time.

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.

## Initial Output

You can use ROS 2’s `tf2` system to transform a `PointStamped` from the hallway camera frame into the robot’s `base_link` frame. The TF buffer stores the relationship between coordinate frames and can transform the point into the requested target frame.

```python
from geometry_msgs.msg import PointStamped

def transform_camera_point(tf_buffer, point: PointStamped):
    return tf_buffer.transform(point, "base_link")
```

This assumes that the TF tree already contains a valid transform between the hallway camera and `base_link`, and that the incoming point has the correct camera frame set in its `header.frame_id`.


## Initial Source

from geometry_msgs.msg import PointStamped

def transform_camera_point(tf_buffer, point: PointStamped):
    return tf_buffer.transform(point, "base_link")

## Initial Analysis

The response assumes the point already uses "hall_camera", has valid metadata and timestamps, and that the TF buffer already contains a valid transformation to "base_link". It does not handle unavailable transformations. It correctly avoids hard coded offsets and does not use motion topics because this task only transforms coordinates. 

## Improved Changes

The improved prompt clearly requires hall_camera as the source and base_link as the target, preserves the point’s timestamp so TF uses the correct observation time, and requires using the TF buffer instead of hard coded offsets. It also specifies that invalid source frames should raise ValueError, while unavailable transformations should return None without sending any robot motion commands.

## Live Pending

True

## Synthesis

The initial AI output assumed the point already came from hall_camera and that TF data was available. The improved prompt added frame validation, timestamp preservation, TF based transformation to base_link, and failure handling. A wrong transform could place a person or obstacle in the wrong location relative to the robot. The frame/rotation tests detect this. If transform data is unavailable, the robot should not move and the function should return None.

## Snapshot

{'source': 'reference', 'captured_at': '2026-09-22T01:39:22.329691+00:00', 'description': 'Instructor-defined frame geometry. No live ROS transforms were measured.', 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'transforms': {'base_scan_to_base_link': {'translation': {'x': 0.2, 'y': 0.0, 'z': 0.14}, 'yaw': 0.0}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': 3.141592653589793}, 'hall_camera_to_base_link': {'translation': {'x': -1.5, 'y': 0.5, 'z': 1.2}, 'yaw': -1.5707963267948966}}}

## Live Issue

The five course tests passed, but the live check returned point: null and live_passed: false. I verified that the hall_camera to base_link transformation was available using tf2_echo, and I also retried the live evaluator with ROS_DOMAIN_ID=25 and simulation time enabled. The live check still did not complete. The remaining unverified part is whether the current hallway camera observation can be transformed successfully during the live evaluator run.
