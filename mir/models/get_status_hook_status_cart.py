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


class GetStatusHookStatusCart(object):
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
        'id': 'float',
        'length': 'float',
        'width': 'float',
        'height': 'float',
        'offset_locked_wheels': 'float'
    }

    attribute_map = {
        'id': 'id',
        'length': 'length',
        'width': 'width',
        'height': 'height',
        'offset_locked_wheels': 'offset_locked_wheels'
    }

    def __init__(self, id=None, length=None, width=None, height=None, offset_locked_wheels=None, _configuration=None):  # noqa: E501
        """GetStatusHookStatusCart - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._length = None
        self._width = None
        self._height = None
        self._offset_locked_wheels = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if length is not None:
            self.length = length
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if offset_locked_wheels is not None:
            self.offset_locked_wheels = offset_locked_wheels

    @property
    def id(self):
        """Gets the id of this GetStatusHookStatusCart.  # noqa: E501

        The id of the attached trolley  # noqa: E501

        :return: The id of this GetStatusHookStatusCart.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetStatusHookStatusCart.

        The id of the attached trolley  # noqa: E501

        :param id: The id of this GetStatusHookStatusCart.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def length(self):
        """Gets the length of this GetStatusHookStatusCart.  # noqa: E501

        The length of the attached trolley  # noqa: E501

        :return: The length of this GetStatusHookStatusCart.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this GetStatusHookStatusCart.

        The length of the attached trolley  # noqa: E501

        :param length: The length of this GetStatusHookStatusCart.  # noqa: E501
        :type: float
        """

        self._length = length

    @property
    def width(self):
        """Gets the width of this GetStatusHookStatusCart.  # noqa: E501

        The width of the attached trolley  # noqa: E501

        :return: The width of this GetStatusHookStatusCart.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this GetStatusHookStatusCart.

        The width of the attached trolley  # noqa: E501

        :param width: The width of this GetStatusHookStatusCart.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this GetStatusHookStatusCart.  # noqa: E501

        The height of the attached trolley  # noqa: E501

        :return: The height of this GetStatusHookStatusCart.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this GetStatusHookStatusCart.

        The height of the attached trolley  # noqa: E501

        :param height: The height of this GetStatusHookStatusCart.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def offset_locked_wheels(self):
        """Gets the offset_locked_wheels of this GetStatusHookStatusCart.  # noqa: E501

        The distance from front of the attached trolley to the locked wheels  # noqa: E501

        :return: The offset_locked_wheels of this GetStatusHookStatusCart.  # noqa: E501
        :rtype: float
        """
        return self._offset_locked_wheels

    @offset_locked_wheels.setter
    def offset_locked_wheels(self, offset_locked_wheels):
        """Sets the offset_locked_wheels of this GetStatusHookStatusCart.

        The distance from front of the attached trolley to the locked wheels  # noqa: E501

        :param offset_locked_wheels: The offset_locked_wheels of this GetStatusHookStatusCart.  # noqa: E501
        :type: float
        """

        self._offset_locked_wheels = offset_locked_wheels

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
        if issubclass(GetStatusHookStatusCart, dict):
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
        if not isinstance(other, GetStatusHookStatusCart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetStatusHookStatusCart):
            return True

        return self.to_dict() != other.to_dict()
