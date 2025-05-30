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
from mir.api.metrics_api import MetricsApi  # noqa: E501
from mir.rest import ApiException


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = mir.api.metrics_api.MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_metrics_get(self):
        """Test case for metrics_get

        GET /metrics  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
