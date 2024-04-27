from unittest import TestCase
import square

class TestSquare(TestCase):

    def test_square(self):
        self.assertEqual(4, square.square(2))
