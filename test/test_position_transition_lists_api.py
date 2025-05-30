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
from mir.api.position_transition_lists_api import PositionTransitionListsApi  # noqa: E501
from mir.rest import ApiException


class TestPositionTransitionListsApi(unittest.TestCase):
    """PositionTransitionListsApi unit test stubs"""

    def setUp(self):
        self.api = mir.api.position_transition_lists_api.PositionTransitionListsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_position_transition_lists_get(self):
        """Test case for position_transition_lists_get

        GET /position_transition_lists  # noqa: E501
        """
        pass

    def test_position_transition_lists_guid_delete(self):
        """Test case for position_transition_lists_guid_delete

        DELETE /position_transition_lists/{guid}  # noqa: E501
        """
        pass

    def test_position_transition_lists_guid_get(self):
        """Test case for position_transition_lists_guid_get

        GET /position_transition_lists/{guid}  # noqa: E501
        """
        pass

    def test_position_transition_lists_guid_put(self):
        """Test case for position_transition_lists_guid_put

        PUT /position_transition_lists/{guid}  # noqa: E501
        """
        pass

    def test_position_transition_lists_post(self):
        """Test case for position_transition_lists_post

        POST /position_transition_lists  # noqa: E501
        """
        pass

    def test_sessions_session_id_position_transition_lists_get(self):
        """Test case for sessions_session_id_position_transition_lists_get

        GET /sessions/{session_id}/position_transition_lists  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
