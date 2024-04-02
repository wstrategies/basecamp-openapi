# coding: utf-8

"""
    Basecamp4 API

    This is an API schema for the Basecamp4 API. It is used to generate client libraries to interact with the API.

    The version of the OpenAPI document: 1.0.0
    Contact: barry@wstrategies.co
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from basecamp4_python_sdk.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_authorization_json_get(self) -> None:
        """Test case for authorization_json_get

        Get authorization
        """
        pass

    def test_projects_json_get(self) -> None:
        """Test case for projects_json_get

        Get projects
        """
        pass


if __name__ == '__main__':
    unittest.main()