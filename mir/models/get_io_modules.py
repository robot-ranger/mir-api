# coding: utf-8

"""
    3.5.4 MIR250 REST API

    The REST API for the 3.5.4 interface of MIR250  # noqa: E501

    OpenAPI spec version: 3.5.4
    Contact: support@mir-robots.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mir.configuration import Configuration


class GetIoModules(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'str',
        'guid': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'url': 'url',
        'guid': 'guid',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, url=None, guid=None, name=None, type=None, _configuration=None):  # noqa: E501
        """GetIoModules - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._url = None
        self._guid = None
        self._name = None
        self._type = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if guid is not None:
            self.guid = guid
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def url(self):
        """Gets the url of this GetIoModules.  # noqa: E501

        The URL of the resource  # noqa: E501

        :return: The url of this GetIoModules.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetIoModules.

        The URL of the resource  # noqa: E501

        :param url: The url of this GetIoModules.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def guid(self):
        """Gets the guid of this GetIoModules.  # noqa: E501

        The global unique id across robots that identifies this io module  # noqa: E501

        :return: The guid of this GetIoModules.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetIoModules.

        The global unique id across robots that identifies this io module  # noqa: E501

        :param guid: The guid of this GetIoModules.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def name(self):
        """Gets the name of this GetIoModules.  # noqa: E501

        The name of the io module  # noqa: E501

        :return: The name of this GetIoModules.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetIoModules.

        The name of the io module  # noqa: E501

        :param name: The name of this GetIoModules.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this GetIoModules.  # noqa: E501

        The type of the io module. currently supported devices [wise].  # noqa: E501

        :return: The type of this GetIoModules.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetIoModules.

        The type of the io module. currently supported devices [wise].  # noqa: E501

        :param type: The type of this GetIoModules.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetIoModules, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetIoModules):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetIoModules):
            return True

        return self.to_dict() != other.to_dict()
