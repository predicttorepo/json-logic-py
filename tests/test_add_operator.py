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
    
    def test_json_operator(self):

        self.assertEqual({"a": 1, "b": 2, "c": 3}, jsonLogic({"json_root": [["a", "b", "c"], [1, 2, 3]]}))
    
    def test_json_operator_with_jsonlogic(self):

        data = {"a": 1, "b": 2, "c": 3}
        out = jsonLogic({"json_root": [["a", "b", "c"],
                                  [{"var": "a"}, {"var": "b"}, {"var": "c"}]
                                  ]}, data)
        self.assertEqual(data, out)
    
    def test_jsonoperator_with_jsonoperator(self):
        
        data = {"a": 1, "b": 2, "c": {'ca': 30, 'cb': 31, 'cc': {"cca": 300, "ccb": 301}}}
        out = jsonLogic({"json_root": [["a", "b", "c"],
                                       [{"var": "a"},
                                        {"var": "b"},
                                        {"json_node": [["ca", "cb", "cc"], [{"var": "c.ca"},
                                                                            {"var": "c.cb"},
                                                                            {"json_node": [["cca", "ccb"],
                                                                                           [{"var": "c.cc.cca"},
                                                                                            {"var": "c.cc.ccb"}]]
                                                                             }]]
                                         }
                                        ]]
                         }, data)
        
        self.assertEqual(data, out)
