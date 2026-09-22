from geometry_msgs.msg import PointStamped

def transform_camera_point(tf_buffer, point: PointStamped):
    return tf_buffer.transform(point, "base_link")