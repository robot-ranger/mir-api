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
from mir.api.sessions_api import SessionsApi  # noqa: E501
from mir.rest import ApiException


class TestSessionsApi(unittest.TestCase):
    """SessionsApi unit test stubs"""

    def setUp(self):
        self.api = mir.api.sessions_api.SessionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sessions_get(self):
        """Test case for sessions_get

        GET /sessions  # noqa: E501
        """
        pass

    def test_sessions_guid_delete(self):
        """Test case for sessions_guid_delete

        DELETE /sessions/{guid}  # noqa: E501
        """
        pass

    def test_sessions_guid_export_get(self):
        """Test case for sessions_guid_export_get

        GET /sessions/{guid}/export  # noqa: E501
        """
        pass

    def test_sessions_guid_get(self):
        """Test case for sessions_guid_get

        GET /sessions/{guid}  # noqa: E501
        """
        pass

    def test_sessions_guid_put(self):
        """Test case for sessions_guid_put

        PUT /sessions/{guid}  # noqa: E501
        """
        pass

    def test_sessions_import_delete(self):
        """Test case for sessions_import_delete

        DELETE /sessions/import  # noqa: E501
        """
        pass

    def test_sessions_import_get(self):
        """Test case for sessions_import_get

        GET /sessions/import  # noqa: E501
        """
        pass

    def test_sessions_import_post(self):
        """Test case for sessions_import_post

        POST /sessions/import  # noqa: E501
        """
        pass

    def test_sessions_post(self):
        """Test case for sessions_post

        POST /sessions  # noqa: E501
        """
        pass

    def test_sessions_session_id_elevator_floors_get(self):
        """Test case for sessions_session_id_elevator_floors_get

        GET /sessions/{session_id}/elevator_floors  # noqa: E501
        """
        pass

    def test_sessions_session_id_elevators_get(self):
        """Test case for sessions_session_id_elevators_get

        GET /sessions/{session_id}/elevators  # noqa: E501
        """
        pass

    def test_sessions_session_id_maps_get(self):
        """Test case for sessions_session_id_maps_get

        GET /sessions/{session_id}/maps  # noqa: E501
        """
        pass

    def test_sessions_session_id_missions_get(self):
        """Test case for sessions_session_id_missions_get

        GET /sessions/{session_id}/missions  # noqa: E501
        """
        pass

    def test_sessions_session_id_position_transition_lists_get(self):
        """Test case for sessions_session_id_position_transition_lists_get

        GET /sessions/{session_id}/position_transition_lists  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
