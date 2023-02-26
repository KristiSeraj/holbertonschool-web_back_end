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
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_get:
            payload = {'repos_url': 'google'}
            mock_get.return_value = payload
            client = GithubOrgClient('hello')
            self.assertEqual(client._public_repos_url, payload['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Testing another public repo method"""
        payload = [{'name': 'Google'}]
        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_get:
            mock_get.return_value = 'test/test'
            client = GithubOrgClient('test')
            el = [i['name'] for i in payload]
            self.assertEqual(client.public_repos(), el)

            mock_get.assert_called_once()
            mock_json.assert_called_once()
