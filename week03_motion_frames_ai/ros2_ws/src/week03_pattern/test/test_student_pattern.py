import math
import os
import unittest

from week03_pattern.pattern import build_pattern


class MyPatternTests(unittest.TestCase):
    def test_my_pattern_geometry(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])

        self.assertEqual(len(segments), 4)

        for segment in segments:
            self.assertGreater(segment.linear_x, 0.0)
            self.assertNotEqual(segment.angular_z, 0.0)

            radius = abs(segment.linear_x / segment.angular_z)
            angle = abs(segment.angular_z * segment.duration)

            self.assertAlmostEqual(radius, 0.30, places=3)
            self.assertAlmostEqual(angle, math.pi / 4, places=3)

    def test_my_pattern_order(self):
        segments = build_pattern(os.environ["WEEK03_ASSIGNED_PATTERN"])

        turn_signs = [
            1 if segment.angular_z > 0 else -1
            for segment in segments
        ]

        self.assertEqual(turn_signs, [1, -1, 1, -1])

        net_heading = sum(
            segment.angular_z * segment.duration
            for segment in segments
        )

        self.assertAlmostEqual(net_heading, 0.0, places=3)


if __name__ == "__main__":
    unittest.main()