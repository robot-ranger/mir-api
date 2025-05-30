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
from mir.api.upgrades_api import UpgradesApi  # noqa: E501
from mir.rest import ApiException


class TestUpgradesApi(unittest.TestCase):
    """UpgradesApi unit test stubs"""

    def setUp(self):
        self.api = mir.api.upgrades_api.UpgradesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_software_upgrades_get(self):
        """Test case for software_upgrades_get

        GET /software/upgrades  # noqa: E501
        """
        pass

    def test_software_upgrades_guid_delete(self):
        """Test case for software_upgrades_guid_delete

        DELETE /software/upgrades/{guid}  # noqa: E501
        """
        pass

    def test_software_upgrades_guid_get(self):
        """Test case for software_upgrades_guid_get

        GET /software/upgrades/{guid}  # noqa: E501
        """
        pass

    def test_software_upgrades_guid_post(self):
        """Test case for software_upgrades_guid_post

        POST /software/upgrades/{guid}  # noqa: E501
        """
        pass

    def test_software_upgrades_post(self):
        """Test case for software_upgrades_post

        POST /software/upgrades  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
