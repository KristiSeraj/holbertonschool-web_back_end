#!/usr/bin/env python3
"""Testing module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, mapping, path):
        """Raises KeyError if key doesn't exist"""
        with self.assertRaises(KeyError):
            access_nested_map(mapping, path)


class TestGetJson(unittest.TestCase):
    """Get_Json test case class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Tests get json method"""
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
