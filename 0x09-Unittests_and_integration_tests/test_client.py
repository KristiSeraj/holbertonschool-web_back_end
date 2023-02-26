#!/usr/bin/env python3
"""Test client methods"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Test githuborgclient class"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json', return_value={'payload': True})
    def test_org(self, name, mock_get):
        """Test org method"""
        org = GithubOrgClient(name)
        self.assertEqual(org.org, mock_get.return_value)
        mock_get.assert_called_once

    def test_public_repos_url(self):
        """Testing public repo url method"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_get:
            payload = {'repos_url': 'google'}
            mock_get.return_value = payload
            client = GithubOrgClient('hello')
            self.assertEqual(client._public_repos_url, payload['repos_url'])
