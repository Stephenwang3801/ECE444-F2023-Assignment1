import unittest
from utils import Utils

class TestUtils(unittest.TestCase):
    def test_reversed(self):
        self.assertEqual(Utils.reversed(123), 321)
        self.assertEqual(Utils.reversed('123'), "invalid")
        self.assertEqual(Utils.reversed(12.3), "invalid")
    def test_formatter(self):
        self.assertEqual(Utils.formatter(123), ['0b1111011', '0o173'])
        self.assertEqual(Utils.formatter('123'), "invalid")
        self.assertEqual(Utils.formatter(12.3), "invalid")
unittest.main()