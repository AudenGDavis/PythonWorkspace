import unittest
from ClassNotes.September8th_ClassesAndOOP.September8th_ClassesAndOop import CartesianPoint

# unit tests
# units tests represent an application test as a object that runs a series of test on with data example
class Tester(unittest.TestCase):
    def setUp(self) -> None:
        self.point = CartesianPoint(1,1)

    def test_constructor(self) -> None:
        self.assertEqual(self.point.x, 1)
        self.assertEqual(self.point.y, 1)


if __name__ == '__main__':
    unittest.main()