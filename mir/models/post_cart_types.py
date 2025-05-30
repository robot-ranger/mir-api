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


class PostCartTypes(object):
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
        'guid': 'str',
        'name': 'str',
        'length': 'float',
        'width': 'float',
        'height': 'float',
        'offset_locked_wheels': 'float',
        'created_by_id': 'str'
    }

    attribute_map = {
        'guid': 'guid',
        'name': 'name',
        'length': 'length',
        'width': 'width',
        'height': 'height',
        'offset_locked_wheels': 'offset_locked_wheels',
        'created_by_id': 'created_by_id'
    }

    def __init__(self, guid=None, name=None, length=None, width=None, height=None, offset_locked_wheels=None, created_by_id=None, _configuration=None):  # noqa: E501
        """PostCartTypes - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._guid = None
        self._name = None
        self._length = None
        self._width = None
        self._height = None
        self._offset_locked_wheels = None
        self._created_by_id = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.offset_locked_wheels = offset_locked_wheels
        if created_by_id is not None:
            self.created_by_id = created_by_id

    @property
    def guid(self):
        """Gets the guid of this PostCartTypes.  # noqa: E501


        :return: The guid of this PostCartTypes.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this PostCartTypes.


        :param guid: The guid of this PostCartTypes.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def name(self):
        """Gets the name of this PostCartTypes.  # noqa: E501

        Min length: 1, Max length: 40  # noqa: E501

        :return: The name of this PostCartTypes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostCartTypes.

        Min length: 1, Max length: 40  # noqa: E501

        :param name: The name of this PostCartTypes.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def length(self):
        """Gets the length of this PostCartTypes.  # noqa: E501


        :return: The length of this PostCartTypes.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this PostCartTypes.


        :param length: The length of this PostCartTypes.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def width(self):
        """Gets the width of this PostCartTypes.  # noqa: E501


        :return: The width of this PostCartTypes.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this PostCartTypes.


        :param width: The width of this PostCartTypes.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this PostCartTypes.  # noqa: E501


        :return: The height of this PostCartTypes.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this PostCartTypes.


        :param height: The height of this PostCartTypes.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def offset_locked_wheels(self):
        """Gets the offset_locked_wheels of this PostCartTypes.  # noqa: E501


        :return: The offset_locked_wheels of this PostCartTypes.  # noqa: E501
        :rtype: float
        """
        return self._offset_locked_wheels

    @offset_locked_wheels.setter
    def offset_locked_wheels(self, offset_locked_wheels):
        """Sets the offset_locked_wheels of this PostCartTypes.


        :param offset_locked_wheels: The offset_locked_wheels of this PostCartTypes.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and offset_locked_wheels is None:
            raise ValueError("Invalid value for `offset_locked_wheels`, must not be `None`")  # noqa: E501

        self._offset_locked_wheels = offset_locked_wheels

    @property
    def created_by_id(self):
        """Gets the created_by_id of this PostCartTypes.  # noqa: E501


        :return: The created_by_id of this PostCartTypes.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this PostCartTypes.


        :param created_by_id: The created_by_id of this PostCartTypes.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

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
        if issubclass(PostCartTypes, dict):
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
        if not isinstance(other, PostCartTypes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostCartTypes):
            return True

        return self.to_dict() != other.to_dict()
