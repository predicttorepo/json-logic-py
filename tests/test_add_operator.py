"""
Tests for jsonLogic.
"""
import unittest
from json_logic import jsonLogic, add_operator, operations
from math import factorial


class JSONLogicTest(unittest.TestCase):
    def test_add_math_operator(self):
        add_operator("!", factorial)
        self.assertTrue("!" in operations)
        self.assertEqual(24, jsonLogic({"!": [4]}))
        
    def test_add_str_operator(self):
        def split(string, sep, pos):
            return string.split(sep)[pos]
        
        add_operator("split", split)
        self.assertTrue("split" in operations)
        self.assertEqual("b", jsonLogic({"split": ["a|b|c", "|", 1]}))
        