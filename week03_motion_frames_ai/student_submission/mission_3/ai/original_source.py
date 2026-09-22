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