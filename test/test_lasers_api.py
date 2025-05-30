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
from mir.api.lasers_api import LasersApi  # noqa: E501
from mir.rest import ApiException


class TestLasersApi(unittest.TestCase):
    """LasersApi unit test stubs"""

    def setUp(self):
        self.api = mir.api.lasers_api.LasersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_system_setup_serial_devices_lasers_get(self):
        """Test case for system_setup_serial_devices_lasers_get

        GET /system/setup/serial_devices/lasers  # noqa: E501
        """
        pass

    def test_system_setup_serial_devices_lasers_put(self):
        """Test case for system_setup_serial_devices_lasers_put

        PUT /system/setup/serial_devices/lasers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
