import unittest
from roman_numeral import romanumeralise

class TestStingMethods(unittest.TestCase):
    def test_does_output(self):
        self.assertEqual(romanumeralise(1), "I")
    def test_ouputs_II(self):
        self.assertEqual(romanumeralise(2), "II")
    def test_outputs_III(self):
        self.assertEqual(romanumeralise(3), "III")