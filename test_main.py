import unittest

class TestHR(unittest.TestCase):
    def test_obliczen(self):
        # Test: 40 godzin * 100 zł = 4000 zł
        self.assertEqual(40 * 100, 4000)

if __name__ == '__main__':
    unittest.main()