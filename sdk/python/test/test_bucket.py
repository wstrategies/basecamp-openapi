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
import datetime

from basecamp4_python_sdk.models.bucket import Bucket

class TestBucket(unittest.TestCase):
    """Bucket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Bucket:
        """Test Bucket
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Bucket`
        """
        model = Bucket()
        if include_optional:
            return Bucket(
                id = 56,
                name = '',
                type = ''
            )
        else:
            return Bucket(
                id = 56,
                name = '',
                type = '',
        )
        """

    def testBucket(self):
        """Test Bucket"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
