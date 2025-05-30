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
from mir.api.networks_api import NetworksApi  # noqa: E501
from mir.rest import ApiException


class TestNetworksApi(unittest.TestCase):
    """NetworksApi unit test stubs"""

    def setUp(self):
        self.api = mir.api.networks_api.NetworksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_wifi_networks_get(self):
        """Test case for wifi_networks_get

        GET /wifi/networks  # noqa: E501
        """
        pass

    def test_wifi_networks_guid_get(self):
        """Test case for wifi_networks_guid_get

        GET /wifi/networks/{guid}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
