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

from basecamp4_python_sdk.models.authorization import Authorization

class TestAuthorization(unittest.TestCase):
    """Authorization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Authorization:
        """Test Authorization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Authorization`
        """
        model = Authorization()
        if include_optional:
            return Authorization(
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                identity = basecamp4_python_sdk.models.identity.Identity(
                    id = 56, 
                    first_name = '', 
                    last_name = '', 
                    email_address = '', ),
                accounts = [
                    basecamp4_python_sdk.models.account.Account(
                        product = '', 
                        id = 56, 
                        name = '', 
                        href = '', 
                        app_href = '', )
                    ]
            )
        else:
            return Authorization(
        )
        """

    def testAuthorization(self):
        """Test Authorization"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
