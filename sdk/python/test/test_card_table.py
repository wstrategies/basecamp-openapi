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

from basecamp4_python_sdk.models.card_table import CardTable

class TestCardTable(unittest.TestCase):
    """CardTable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CardTable:
        """Test CardTable
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CardTable`
        """
        model = CardTable()
        if include_optional:
            return CardTable(
                id = 56,
                status = '',
                visible_to_clients = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                title = '',
                inherits_status = True,
                type = '',
                url = '',
                app_url = '',
                bookmark_url = '',
                subscription_url = '',
                bucket = basecamp4_python_sdk.models.bucket.Bucket(
                    id = 56, 
                    name = '', 
                    type = '', ),
                creator = basecamp4_python_sdk.models.person.Person(
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
                    can_manage_people = True, ),
                subscribers = [
                    basecamp4_python_sdk.models.person.Person(
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
                        can_manage_people = True, )
                    ],
                lists = [
                    basecamp4_python_sdk.models.card_table_column.CardTableColumn(
                        id = 56, 
                        status = '', 
                        visible_to_clients = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        title = '', 
                        inherits_status = True, 
                        type = '', 
                        url = '', 
                        app_url = '', 
                        bookmark_url = '', 
                        parent = basecamp4_python_sdk.models.card_table.CardTable(
                            id = 56, 
                            status = '', 
                            visible_to_clients = True, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            title = '', 
                            inherits_status = True, 
                            type = '', 
                            url = '', 
                            app_url = '', 
                            bookmark_url = '', 
                            subscription_url = '', 
                            bucket = basecamp4_python_sdk.models.bucket.Bucket(
                                id = 56, 
                                name = '', 
                                type = '', ), 
                            creator = basecamp4_python_sdk.models.person.Person(
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
                                can_manage_people = True, ), 
                            subscribers = [
                                basecamp4_python_sdk.models.person.Person(
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
                                    can_manage_projects = True, 
                                    can_manage_people = True, )
                                ], 
                            lists = [
                                basecamp4_python_sdk.models.card_table_column.CardTableColumn(
                                    id = 56, 
                                    status = '', 
                                    visible_to_clients = True, 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    title = '', 
                                    inherits_status = True, 
                                    type = '', 
                                    url = '', 
                                    app_url = '', 
                                    bookmark_url = '', 
                                    description = '', 
                                    color = '', 
                                    cards_count = 56, 
                                    comment_count = 56, 
                                    cards_url = '', )
                                ], ), 
                        bucket = basecamp4_python_sdk.models.bucket.Bucket(
                            id = 56, 
                            name = '', 
                            type = '', ), 
                        creator = , 
                        description = '', 
                        subscribers = [
                            
                            ], 
                        color = '', 
                        cards_count = 56, 
                        comment_count = 56, 
                        cards_url = '', )
                    ]
            )
        else:
            return CardTable(
                id = 56,
        )
        """

    def testCardTable(self):
        """Test CardTable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
