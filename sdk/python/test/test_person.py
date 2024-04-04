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

from basecamp4_python_sdk.models.person import Person

class TestPerson(unittest.TestCase):
    """Person unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Person:
        """Test Person
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Person`
        """
        model = Person()
        if include_optional:
            return Person(
                id = 56,
                attachable_sgid = '',
                name = '',
                email_address = '',
                personable_type = '',
                title = '',
                bio = '',
                location = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                admin = True,
                owner = True,
                client = True,
                employee = True,
                time_zone = '',
                avatar_url = '',
                company = basecamp4_python_sdk.models.company.Company(
                    id = 56, 
                    name = '', ),
                can_manage_projects = True,
                can_manage_people = True
            )
        else:
            return Person(
                id = 56,
                name = '',
                email_address = '',
                personable_type = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testPerson(self):
        """Test Person"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()