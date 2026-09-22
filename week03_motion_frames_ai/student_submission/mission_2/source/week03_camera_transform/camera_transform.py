"""Transform hallway-camera points into the robot base frame."""

from geometry_msgs.msg import PointStamped
import tf2_geometry_msgs
from tf2_ros import TransformException


def transform_camera_point(
    tf_buffer,
    point: PointStamped,
) -> PointStamped | None:
    """Transform a hall_camera point into base_link."""

    if point.header.frame_id != "hall_camera":
        raise ValueError("Expected point in hall_camera frame")

    try:
        return tf_buffer.transform(point, "base_link")
    except TransformException:
        return None