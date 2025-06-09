import unittest
from roman_numeral import romanumeralise

class TestStingMethods(unittest.TestCase):
    def test_does_output(self):
        self.assertEqual(romanumeralise(1), "I")