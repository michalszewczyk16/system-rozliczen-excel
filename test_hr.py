import unittest

class TestHR(unittest.TestCase):
    def test_obliczen(self):

        self.assertEqual(40 * 100, 4000)

    def test_wynagrodzenia_zero(self):

        self.assertEqual(0 * 100, 0)

if __name__ == '__main__':
    unittest.main()