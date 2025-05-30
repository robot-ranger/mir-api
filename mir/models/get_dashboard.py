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


class GetDashboard(object):
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
        'fleet_dashboard': 'bool',
        'widgets': 'str',
        'created_by_id': 'str',
        'created_by': 'str'
    }

    attribute_map = {
        'guid': 'guid',
        'name': 'name',
        'fleet_dashboard': 'fleet_dashboard',
        'widgets': 'widgets',
        'created_by_id': 'created_by_id',
        'created_by': 'created_by'
    }

    def __init__(self, guid=None, name=None, fleet_dashboard=None, widgets=None, created_by_id=None, created_by=None, _configuration=None):  # noqa: E501
        """GetDashboard - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._guid = None
        self._name = None
        self._fleet_dashboard = None
        self._widgets = None
        self._created_by_id = None
        self._created_by = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if name is not None:
            self.name = name
        if fleet_dashboard is not None:
            self.fleet_dashboard = fleet_dashboard
        if widgets is not None:
            self.widgets = widgets
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_by is not None:
            self.created_by = created_by

    @property
    def guid(self):
        """Gets the guid of this GetDashboard.  # noqa: E501

        The global id unique across robots that identifies this dashboard  # noqa: E501

        :return: The guid of this GetDashboard.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetDashboard.

        The global id unique across robots that identifies this dashboard  # noqa: E501

        :param guid: The guid of this GetDashboard.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def name(self):
        """Gets the name of this GetDashboard.  # noqa: E501

        The name of this dashboard  # noqa: E501

        :return: The name of this GetDashboard.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetDashboard.

        The name of this dashboard  # noqa: E501

        :param name: The name of this GetDashboard.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def fleet_dashboard(self):
        """Gets the fleet_dashboard of this GetDashboard.  # noqa: E501

          # noqa: E501

        :return: The fleet_dashboard of this GetDashboard.  # noqa: E501
        :rtype: bool
        """
        return self._fleet_dashboard

    @fleet_dashboard.setter
    def fleet_dashboard(self, fleet_dashboard):
        """Sets the fleet_dashboard of this GetDashboard.

          # noqa: E501

        :param fleet_dashboard: The fleet_dashboard of this GetDashboard.  # noqa: E501
        :type: bool
        """

        self._fleet_dashboard = fleet_dashboard

    @property
    def widgets(self):
        """Gets the widgets of this GetDashboard.  # noqa: E501

        The url to the possible widgets. if the dashboard does not have any widgets then this field is empty  # noqa: E501

        :return: The widgets of this GetDashboard.  # noqa: E501
        :rtype: str
        """
        return self._widgets

    @widgets.setter
    def widgets(self, widgets):
        """Sets the widgets of this GetDashboard.

        The url to the possible widgets. if the dashboard does not have any widgets then this field is empty  # noqa: E501

        :param widgets: The widgets of this GetDashboard.  # noqa: E501
        :type: str
        """

        self._widgets = widgets

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetDashboard.  # noqa: E501

        The global id of the user who created this entry  # noqa: E501

        :return: The created_by_id of this GetDashboard.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetDashboard.

        The global id of the user who created this entry  # noqa: E501

        :param created_by_id: The created_by_id of this GetDashboard.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_by(self):
        """Gets the created_by of this GetDashboard.  # noqa: E501

        The url to the user that created the dashboard  # noqa: E501

        :return: The created_by of this GetDashboard.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetDashboard.

        The url to the user that created the dashboard  # noqa: E501

        :param created_by: The created_by of this GetDashboard.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

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
        if issubclass(GetDashboard, dict):
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
        if not isinstance(other, GetDashboard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDashboard):
            return True

        return self.to_dict() != other.to_dict()
