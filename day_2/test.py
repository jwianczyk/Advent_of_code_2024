import unittest
import main


# 593 - Too high
class TestPart1(unittest.TestCase):
    def test1(self):
        input = [[7, 6, 4, 2, 1],
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
                [1, 3, 6, 7, 9]]   
        res = main.day2(input)
        print(res)
        assert res == 2
    
    def test2(self):
        input = [7, 6, 4, 2, 1]
        res = main.check_list(input)
        assert res is True

    def test3(self):
        input = [1, 2, 7, 8, 9]
        res = main.check_list(input)
        assert res is False

    def test4(self):
        input = [1, 3, 2, 4, 5]
        res = main.check_list(input)
        assert res is False

    def test5(self):
        input = [1, 3, 6, 7, 9]
        res = main.check_list(input)
        assert res is True

    def test6(self):
        input = [96, 94, 93, 92, 91, 90, 87, 90]
        res = main.check_list(input)
        assert res is False

    def test7(self):
        input = [95, 96, 99, 97, 96, 95, 94, 96]
        res = main.check_list(input)
        assert res is False
class TestPart2(unittest.TestCase):
    def test1(self):
        pass