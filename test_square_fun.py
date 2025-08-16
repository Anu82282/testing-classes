import unittest
from unit_test_squ_fun import *
class TestSquare(unittest.TestCase):
    def test_square(self):
        data=func_square(2,4)
        assert data == (4,20)
