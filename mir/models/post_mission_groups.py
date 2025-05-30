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


class PostMissionGroups(object):
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
        'priority': 'int',
        'feature': 'str',
        'icon': 'str',
        'created_by_id': 'str'
    }

    attribute_map = {
        'guid': 'guid',
        'name': 'name',
        'priority': 'priority',
        'feature': 'feature',
        'icon': 'icon',
        'created_by_id': 'created_by_id'
    }

    def __init__(self, guid=None, name=None, priority=None, feature=None, icon=None, created_by_id=None, _configuration=None):  # noqa: E501
        """PostMissionGroups - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._guid = None
        self._name = None
        self._priority = None
        self._feature = None
        self._icon = None
        self._created_by_id = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        self.name = name
        self.priority = priority
        self.feature = feature
        self.icon = icon
        if created_by_id is not None:
            self.created_by_id = created_by_id

    @property
    def guid(self):
        """Gets the guid of this PostMissionGroups.  # noqa: E501


        :return: The guid of this PostMissionGroups.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this PostMissionGroups.


        :param guid: The guid of this PostMissionGroups.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def name(self):
        """Gets the name of this PostMissionGroups.  # noqa: E501

        Min length: 1, Max length: 63  # noqa: E501

        :return: The name of this PostMissionGroups.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostMissionGroups.

        Min length: 1, Max length: 63  # noqa: E501

        :param name: The name of this PostMissionGroups.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def priority(self):
        """Gets the priority of this PostMissionGroups.  # noqa: E501


        :return: The priority of this PostMissionGroups.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PostMissionGroups.


        :param priority: The priority of this PostMissionGroups.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def feature(self):
        """Gets the feature of this PostMissionGroups.  # noqa: E501

        Min length: 1, Max length: 63  # noqa: E501

        :return: The feature of this PostMissionGroups.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this PostMissionGroups.

        Min length: 1, Max length: 63  # noqa: E501

        :param feature: The feature of this PostMissionGroups.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and feature is None:
            raise ValueError("Invalid value for `feature`, must not be `None`")  # noqa: E501

        self._feature = feature

    @property
    def icon(self):
        """Gets the icon of this PostMissionGroups.  # noqa: E501


        :return: The icon of this PostMissionGroups.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this PostMissionGroups.


        :param icon: The icon of this PostMissionGroups.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and icon is None:
            raise ValueError("Invalid value for `icon`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                icon is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', icon)):  # noqa: E501
            raise ValueError(r"Invalid value for `icon`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._icon = icon

    @property
    def created_by_id(self):
        """Gets the created_by_id of this PostMissionGroups.  # noqa: E501


        :return: The created_by_id of this PostMissionGroups.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this PostMissionGroups.


        :param created_by_id: The created_by_id of this PostMissionGroups.  # noqa: E501
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
        if issubclass(PostMissionGroups, dict):
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
        if not isinstance(other, PostMissionGroups):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostMissionGroups):
            return True

        return self.to_dict() != other.to_dict()
