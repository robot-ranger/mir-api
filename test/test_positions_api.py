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
from mir.api.positions_api import PositionsApi  # noqa: E501
from mir.rest import ApiException


class TestPositionsApi(unittest.TestCase):
    """PositionsApi unit test stubs"""

    def setUp(self):
        self.api = mir.api.positions_api.PositionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_maps_map_id_positions_get(self):
        """Test case for maps_map_id_positions_get

        GET /maps/{map_id}/positions  # noqa: E501
        """
        pass

    def test_path_guides_path_guide_guid_positions_get(self):
        """Test case for path_guides_path_guide_guid_positions_get

        GET /path_guides/{path_guide_guid}/positions  # noqa: E501
        """
        pass

    def test_path_guides_path_guide_guid_positions_guid_delete(self):
        """Test case for path_guides_path_guide_guid_positions_guid_delete

        DELETE /path_guides/{path_guide_guid}/positions/{guid}  # noqa: E501
        """
        pass

    def test_path_guides_path_guide_guid_positions_guid_get(self):
        """Test case for path_guides_path_guide_guid_positions_guid_get

        GET /path_guides/{path_guide_guid}/positions/{guid}  # noqa: E501
        """
        pass

    def test_path_guides_path_guide_guid_positions_guid_put(self):
        """Test case for path_guides_path_guide_guid_positions_guid_put

        PUT /path_guides/{path_guide_guid}/positions/{guid}  # noqa: E501
        """
        pass

    def test_path_guides_path_guide_guid_positions_post(self):
        """Test case for path_guides_path_guide_guid_positions_post

        POST /path_guides/{path_guide_guid}/positions  # noqa: E501
        """
        pass

    def test_positions_get(self):
        """Test case for positions_get

        GET /positions  # noqa: E501
        """
        pass

    def test_positions_guid_delete(self):
        """Test case for positions_guid_delete

        DELETE /positions/{guid}  # noqa: E501
        """
        pass

    def test_positions_guid_get(self):
        """Test case for positions_guid_get

        GET /positions/{guid}  # noqa: E501
        """
        pass

    def test_positions_guid_put(self):
        """Test case for positions_guid_put

        PUT /positions/{guid}  # noqa: E501
        """
        pass

    def test_positions_parent_guid_helper_positions_get(self):
        """Test case for positions_parent_guid_helper_positions_get

        GET /positions/{parent_guid}/helper_positions  # noqa: E501
        """
        pass

    def test_positions_pos_id_docking_offsets_get(self):
        """Test case for positions_pos_id_docking_offsets_get

        GET /positions/{pos_id}/docking_offsets  # noqa: E501
        """
        pass

    def test_positions_post(self):
        """Test case for positions_post

        POST /positions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
