import unittest
import math

class Position:
    """represents a point on a 300 by 300 Cartesian plane"""
    def __init__(self, x: int, y: int):
        if x < 0 or x > 300 or y < 0 or y > 300:
            raise ValueError
        else:
            self.x = x
            self.y = y

    def dist_to_0(self) -> float:
        """computes the distance to the origin of this position"""
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
    
    def move(self, x: int, y: int) -> None:
        """shift this postion by the given increments"""
        self.x += x
        self.y += y

class testPositionClass(unittest.TestCase):
    def setUp(self) -> None:
        self.position = Position(0,0)

    def test_out_bounds(self) -> None:
        with self.assertRaises(ValueError):
            self.position = Position(1,-1)
        

    

if __name__ == '__main__':
    unittest.main()