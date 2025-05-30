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


class PutDockingOffset(object):
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
        'name': 'str',
        'x_offset': 'float',
        'y_offset': 'float',
        'orientation_offset': 'float'
    }

    attribute_map = {
        'name': 'name',
        'x_offset': 'x_offset',
        'y_offset': 'y_offset',
        'orientation_offset': 'orientation_offset'
    }

    def __init__(self, name=None, x_offset=None, y_offset=None, orientation_offset=None, _configuration=None):  # noqa: E501
        """PutDockingOffset - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._x_offset = None
        self._y_offset = None
        self._orientation_offset = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if x_offset is not None:
            self.x_offset = x_offset
        if y_offset is not None:
            self.y_offset = y_offset
        if orientation_offset is not None:
            self.orientation_offset = orientation_offset

    @property
    def name(self):
        """Gets the name of this PutDockingOffset.  # noqa: E501

        Min length: 1, Max length: 255  # noqa: E501

        :return: The name of this PutDockingOffset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutDockingOffset.

        Min length: 1, Max length: 255  # noqa: E501

        :param name: The name of this PutDockingOffset.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def x_offset(self):
        """Gets the x_offset of this PutDockingOffset.  # noqa: E501


        :return: The x_offset of this PutDockingOffset.  # noqa: E501
        :rtype: float
        """
        return self._x_offset

    @x_offset.setter
    def x_offset(self, x_offset):
        """Sets the x_offset of this PutDockingOffset.


        :param x_offset: The x_offset of this PutDockingOffset.  # noqa: E501
        :type: float
        """

        self._x_offset = x_offset

    @property
    def y_offset(self):
        """Gets the y_offset of this PutDockingOffset.  # noqa: E501


        :return: The y_offset of this PutDockingOffset.  # noqa: E501
        :rtype: float
        """
        return self._y_offset

    @y_offset.setter
    def y_offset(self, y_offset):
        """Sets the y_offset of this PutDockingOffset.


        :param y_offset: The y_offset of this PutDockingOffset.  # noqa: E501
        :type: float
        """

        self._y_offset = y_offset

    @property
    def orientation_offset(self):
        """Gets the orientation_offset of this PutDockingOffset.  # noqa: E501


        :return: The orientation_offset of this PutDockingOffset.  # noqa: E501
        :rtype: float
        """
        return self._orientation_offset

    @orientation_offset.setter
    def orientation_offset(self, orientation_offset):
        """Sets the orientation_offset of this PutDockingOffset.


        :param orientation_offset: The orientation_offset of this PutDockingOffset.  # noqa: E501
        :type: float
        """

        self._orientation_offset = orientation_offset

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
        if issubclass(PutDockingOffset, dict):
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
        if not isinstance(other, PutDockingOffset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutDockingOffset):
            return True

        return self.to_dict() != other.to_dict()
