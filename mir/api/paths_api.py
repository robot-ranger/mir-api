# coding: utf-8

"""
    3.5.4 MIR250 REST API

    The REST API for the 3.5.4 interface of MIR250  # noqa: E501

    OpenAPI spec version: 3.5.4
    Contact: support@mir-robots.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mir.api_client import ApiClient


class PathsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def maps_map_id_paths_get(self, authorization, accept_language, map_id, **kwargs):  # noqa: E501
        """GET /maps/{map_id}/paths  # noqa: E501

        Retrieve the list of paths that belong to the map with the specified map ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.maps_map_id_paths_get(authorization, accept_language, map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :param str map_id: The map_id to search for (required)
        :return: list[GetMapPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.maps_map_id_paths_get_with_http_info(authorization, accept_language, map_id, **kwargs)  # noqa: E501
        else:
            (data) = self.maps_map_id_paths_get_with_http_info(authorization, accept_language, map_id, **kwargs)  # noqa: E501
            return data

    def maps_map_id_paths_get_with_http_info(self, authorization, accept_language, map_id, **kwargs):  # noqa: E501
        """GET /maps/{map_id}/paths  # noqa: E501

        Retrieve the list of paths that belong to the map with the specified map ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.maps_map_id_paths_get_with_http_info(authorization, accept_language, map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :param str map_id: The map_id to search for (required)
        :return: list[GetMapPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'accept_language', 'map_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method maps_map_id_paths_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `maps_map_id_paths_get`")  # noqa: E501
        # verify the required parameter 'accept_language' is set
        if self.api_client.client_side_validation and ('accept_language' not in params or
                                                       params['accept_language'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `accept_language` when calling `maps_map_id_paths_get`")  # noqa: E501
        # verify the required parameter 'map_id' is set
        if self.api_client.client_side_validation and ('map_id' not in params or
                                                       params['map_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `map_id` when calling `maps_map_id_paths_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'map_id' in params:
            path_params['map_id'] = params['map_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/maps/{map_id}/paths', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetMapPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def paths_get(self, authorization, accept_language, **kwargs):  # noqa: E501
        """GET /paths  # noqa: E501

        Retrieve the list of paths  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paths_get(authorization, accept_language, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :return: list[GetPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.paths_get_with_http_info(authorization, accept_language, **kwargs)  # noqa: E501
        else:
            (data) = self.paths_get_with_http_info(authorization, accept_language, **kwargs)  # noqa: E501
            return data

    def paths_get_with_http_info(self, authorization, accept_language, **kwargs):  # noqa: E501
        """GET /paths  # noqa: E501

        Retrieve the list of paths  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paths_get_with_http_info(authorization, accept_language, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :return: list[GetPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'accept_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method paths_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `paths_get`")  # noqa: E501
        # verify the required parameter 'accept_language' is set
        if self.api_client.client_side_validation and ('accept_language' not in params or
                                                       params['accept_language'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `accept_language` when calling `paths_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/paths', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[GetPaths]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def paths_guid_delete(self, authorization, accept_language, guid, **kwargs):  # noqa: E501
        """DELETE /paths/{guid}  # noqa: E501

        Erase the path with the specified GUID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paths_guid_delete(authorization, accept_language, guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :param str guid: The guid to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.paths_guid_delete_with_http_info(authorization, accept_language, guid, **kwargs)  # noqa: E501
        else:
            (data) = self.paths_guid_delete_with_http_info(authorization, accept_language, guid, **kwargs)  # noqa: E501
            return data

    def paths_guid_delete_with_http_info(self, authorization, accept_language, guid, **kwargs):  # noqa: E501
        """DELETE /paths/{guid}  # noqa: E501

        Erase the path with the specified GUID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paths_guid_delete_with_http_info(authorization, accept_language, guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :param str guid: The guid to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'accept_language', 'guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method paths_guid_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `paths_guid_delete`")  # noqa: E501
        # verify the required parameter 'accept_language' is set
        if self.api_client.client_side_validation and ('accept_language' not in params or
                                                       params['accept_language'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `accept_language` when calling `paths_guid_delete`")  # noqa: E501
        # verify the required parameter 'guid' is set
        if self.api_client.client_side_validation and ('guid' not in params or
                                                       params['guid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `guid` when calling `paths_guid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'guid' in params:
            path_params['guid'] = params['guid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/paths/{guid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def paths_guid_get(self, authorization, accept_language, guid, **kwargs):  # noqa: E501
        """GET /paths/{guid}  # noqa: E501

        Retrieve the path with the specified GUID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paths_guid_get(authorization, accept_language, guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :param str guid: The guid to search for (required)
        :return: GetPath
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.paths_guid_get_with_http_info(authorization, accept_language, guid, **kwargs)  # noqa: E501
        else:
            (data) = self.paths_guid_get_with_http_info(authorization, accept_language, guid, **kwargs)  # noqa: E501
            return data

    def paths_guid_get_with_http_info(self, authorization, accept_language, guid, **kwargs):  # noqa: E501
        """GET /paths/{guid}  # noqa: E501

        Retrieve the path with the specified GUID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paths_guid_get_with_http_info(authorization, accept_language, guid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :param str guid: The guid to search for (required)
        :return: GetPath
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'accept_language', 'guid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method paths_guid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `paths_guid_get`")  # noqa: E501
        # verify the required parameter 'accept_language' is set
        if self.api_client.client_side_validation and ('accept_language' not in params or
                                                       params['accept_language'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `accept_language` when calling `paths_guid_get`")  # noqa: E501
        # verify the required parameter 'guid' is set
        if self.api_client.client_side_validation and ('guid' not in params or
                                                       params['guid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `guid` when calling `paths_guid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'guid' in params:
            path_params['guid'] = params['guid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/paths/{guid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPath',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def paths_guid_put(self, authorization, accept_language, guid, path, **kwargs):  # noqa: E501
        """PUT /paths/{guid}  # noqa: E501

        Modify the values of the path with the specified GUID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paths_guid_put(authorization, accept_language, guid, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :param str guid: The guid to modify (required)
        :param PutPath path: The new values of the path (required)
        :return: GetPath
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.paths_guid_put_with_http_info(authorization, accept_language, guid, path, **kwargs)  # noqa: E501
        else:
            (data) = self.paths_guid_put_with_http_info(authorization, accept_language, guid, path, **kwargs)  # noqa: E501
            return data

    def paths_guid_put_with_http_info(self, authorization, accept_language, guid, path, **kwargs):  # noqa: E501
        """PUT /paths/{guid}  # noqa: E501

        Modify the values of the path with the specified GUID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paths_guid_put_with_http_info(authorization, accept_language, guid, path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :param str guid: The guid to modify (required)
        :param PutPath path: The new values of the path (required)
        :return: GetPath
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'accept_language', 'guid', 'path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method paths_guid_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `paths_guid_put`")  # noqa: E501
        # verify the required parameter 'accept_language' is set
        if self.api_client.client_side_validation and ('accept_language' not in params or
                                                       params['accept_language'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `accept_language` when calling `paths_guid_put`")  # noqa: E501
        # verify the required parameter 'guid' is set
        if self.api_client.client_side_validation and ('guid' not in params or
                                                       params['guid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `guid` when calling `paths_guid_put`")  # noqa: E501
        # verify the required parameter 'path' is set
        if self.api_client.client_side_validation and ('path' not in params or
                                                       params['path'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `path` when calling `paths_guid_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'guid' in params:
            path_params['guid'] = params['guid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'path' in params:
            body_params = params['path']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/paths/{guid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPath',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def paths_post(self, authorization, accept_language, paths, **kwargs):  # noqa: E501
        """POST /paths  # noqa: E501

        Add a new path  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paths_post(authorization, accept_language, paths, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :param PostPaths paths: The details of the paths (required)
        :return: GetPaths
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.paths_post_with_http_info(authorization, accept_language, paths, **kwargs)  # noqa: E501
        else:
            (data) = self.paths_post_with_http_info(authorization, accept_language, paths, **kwargs)  # noqa: E501
            return data

    def paths_post_with_http_info(self, authorization, accept_language, paths, **kwargs):  # noqa: E501
        """POST /paths  # noqa: E501

        Add a new path  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.paths_post_with_http_info(authorization, accept_language, paths, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :param PostPaths paths: The details of the paths (required)
        :return: GetPaths
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'accept_language', 'paths']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method paths_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `paths_post`")  # noqa: E501
        # verify the required parameter 'accept_language' is set
        if self.api_client.client_side_validation and ('accept_language' not in params or
                                                       params['accept_language'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `accept_language` when calling `paths_post`")  # noqa: E501
        # verify the required parameter 'paths' is set
        if self.api_client.client_side_validation and ('paths' not in params or
                                                       params['paths'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `paths` when calling `paths_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'accept_language' in params:
            header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'paths' in params:
            body_params = params['paths']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/paths', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPaths',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
