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


class SwaggerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def swagger_get(self, authorization, accept_language, **kwargs):  # noqa: E501
        """GET /swagger  # noqa: E501

        Retrieve the swagger definition of the API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.swagger_get(authorization, accept_language, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :return: GetSwaggerDoc
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.swagger_get_with_http_info(authorization, accept_language, **kwargs)  # noqa: E501
        else:
            (data) = self.swagger_get_with_http_info(authorization, accept_language, **kwargs)  # noqa: E501
            return data

    def swagger_get_with_http_info(self, authorization, accept_language, **kwargs):  # noqa: E501
        """GET /swagger  # noqa: E501

        Retrieve the swagger definition of the API  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.swagger_get_with_http_info(authorization, accept_language, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization header (required)
        :param str accept_language: Language header (required)
        :return: GetSwaggerDoc
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
                    " to method swagger_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if self.api_client.client_side_validation and ('authorization' not in params or
                                                       params['authorization'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `authorization` when calling `swagger_get`")  # noqa: E501
        # verify the required parameter 'accept_language' is set
        if self.api_client.client_side_validation and ('accept_language' not in params or
                                                       params['accept_language'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `accept_language` when calling `swagger_get`")  # noqa: E501

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
            '/swagger', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSwaggerDoc',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
