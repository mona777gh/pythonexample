from Area import area, square
import unittest
from math import pi
class TestArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(0),0)
    def test_value(self):
        self.assertRaises(ValueError,area,-1)
    def test_square(self):
        self.assertAlmostEqual(square(5),25)






