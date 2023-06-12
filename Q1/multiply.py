import unittest


def multiply(x, y):
    if x == 0 or y == 0:
        return 0

    total = 0
    if x < 0:
        [x, y] = [-x, -y]

    while x > 0:
        total += y
        x -= 1

    return total


class TestMultiply(unittest.TestCase):

    def test_0_0(self):
        self.assertEqual(multiply(0, 0), 0)

    def test_0_1(self):
        self.assertEqual(multiply(0, 12), 0)

    def test_1_0(self):
        self.assertEqual(multiply(6, 0), 0)

    def test_negative_x_0(self):
        self.assertEqual(multiply(-6, 0), 0)

    def test_0_negative_y(self):
        self.assertEqual(multiply(0, -12), 0)

    def tet_x_y_positive(self):
        self.assertEqual(multiply(6, 12), 72)

    def test_x_negative(self):
        self.assertEqual(multiply(-6, 12), -72)

    def test_y_negative(self):
        self.assertEqual(multiply(6, -12), -72)

    def test_x_y_negative(self):
        self.assertEqual(multiply(-6, -12), 72)


if __name__ == '__main__':
    unittest.main()
