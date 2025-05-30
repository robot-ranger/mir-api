# coding: utf-8

"""
    3.5.4 MIR250 REST API

    The REST API for the 3.5.4 interface of MIR250  # noqa: E501

    OpenAPI spec version: 3.5.4
    Contact: support@mir-robots.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mir
from mir.api.action_definitions_api import ActionDefinitionsApi  # noqa: E501
from mir.rest import ApiException


class TestActionDefinitionsApi(unittest.TestCase):
    """ActionDefinitionsApi unit test stubs"""

    def setUp(self):
        self.api = mir.api.action_definitions_api.ActionDefinitionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_zones_action_definitions_action_type_get(self):
        """Test case for zones_action_definitions_action_type_get

        GET /zones/action_definitions/{action_type}  # noqa: E501
        """
        pass

    def test_zones_action_definitions_get(self):
        """Test case for zones_action_definitions_get

        GET /zones/action_definitions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
