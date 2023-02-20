#!/usr/bin/env python3
"""Testing module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """AccessNestedMap test case class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, mapping, path, result):
        """Access nested map method that checks for two inputs"""
        self.assertEqual(access_nested_map(mapping, path), result)
