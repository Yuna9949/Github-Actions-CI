import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_subtract_1(self):
        self.assertEqual(example.subtract(5, 2), 3)

    def test_multiply_1(self):
        self.assertEqual(example.multiply(1, 3), 3)

    def test_division_1(self):
        self.assertEqual(example.division(6, 2), 3)


if __name__ == '__main__':
    unittest.main()
