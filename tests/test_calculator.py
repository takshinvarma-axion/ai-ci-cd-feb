import unittest
import sys
from pathlib import Path

import os

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from calculator import add, subtract, multiply, divide, square, square_root, cube, cube_root

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(0, -1), -1)
        self.assertEqual(add(1, -1), 0)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(-1, 0), -1)
    

    # test case that fails for the add function
    # def test_add_failure(self):
    #     self.assertEqual(add(1, 2), 4)