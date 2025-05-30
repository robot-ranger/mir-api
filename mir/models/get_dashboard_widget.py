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


class GetDashboardWidget(object):
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
        'dashboard_id': 'str',
        'dashboard': 'str',
        'settings': 'str',
        'created_by_id': 'str'
    }

    attribute_map = {
        'guid': 'guid',
        'dashboard_id': 'dashboard_id',
        'dashboard': 'dashboard',
        'settings': 'settings',
        'created_by_id': 'created_by_id'
    }

    def __init__(self, guid=None, dashboard_id=None, dashboard=None, settings=None, created_by_id=None, _configuration=None):  # noqa: E501
        """GetDashboardWidget - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._guid = None
        self._dashboard_id = None
        self._dashboard = None
        self._settings = None
        self._created_by_id = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if dashboard is not None:
            self.dashboard = dashboard
        if settings is not None:
            self.settings = settings
        if created_by_id is not None:
            self.created_by_id = created_by_id

    @property
    def guid(self):
        """Gets the guid of this GetDashboardWidget.  # noqa: E501

        The global id unique across robots that identifies this widget  # noqa: E501

        :return: The guid of this GetDashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetDashboardWidget.

        The global id unique across robots that identifies this widget  # noqa: E501

        :param guid: The guid of this GetDashboardWidget.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this GetDashboardWidget.  # noqa: E501

        The guid of the dashboard this widget belongs to  # noqa: E501

        :return: The dashboard_id of this GetDashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this GetDashboardWidget.

        The guid of the dashboard this widget belongs to  # noqa: E501

        :param dashboard_id: The dashboard_id of this GetDashboardWidget.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def dashboard(self):
        """Gets the dashboard of this GetDashboardWidget.  # noqa: E501

        The url to the dashboard where this widget belongs.   # noqa: E501

        :return: The dashboard of this GetDashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._dashboard

    @dashboard.setter
    def dashboard(self, dashboard):
        """Sets the dashboard of this GetDashboardWidget.

        The url to the dashboard where this widget belongs.   # noqa: E501

        :param dashboard: The dashboard of this GetDashboardWidget.  # noqa: E501
        :type: str
        """

        self._dashboard = dashboard

    @property
    def settings(self):
        """Gets the settings of this GetDashboardWidget.  # noqa: E501

        Widgets configuration encoded base 64 in json  # noqa: E501

        :return: The settings of this GetDashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this GetDashboardWidget.

        Widgets configuration encoded base 64 in json  # noqa: E501

        :param settings: The settings of this GetDashboardWidget.  # noqa: E501
        :type: str
        """

        self._settings = settings

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetDashboardWidget.  # noqa: E501

        User guid of the user of the dashboard which the widget belongs to  # noqa: E501

        :return: The created_by_id of this GetDashboardWidget.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetDashboardWidget.

        User guid of the user of the dashboard which the widget belongs to  # noqa: E501

        :param created_by_id: The created_by_id of this GetDashboardWidget.  # noqa: E501
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
        if issubclass(GetDashboardWidget, dict):
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
        if not isinstance(other, GetDashboardWidget):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDashboardWidget):
            return True

        return self.to_dict() != other.to_dict()
