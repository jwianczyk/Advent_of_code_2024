import unittest
import main

class TestPart1(unittest.TestCase):
    def test1(self):
        arr = [3, 4, 2, 1, 3, 3]
        arr2 = [4, 3, 5, 3, 9, 3]
        res, res2 = main.day_1(arr, arr2)
        assert res == 11


class TestPart2(unittest.TestCase):
    def test1(self):
        arr =  [3, 4, 2, 1, 3, 3]
        arr2 = [4, 3, 5, 3, 9, 3]
        res, res2 = main.day_1(arr, arr2)
        assert res2 == 31
