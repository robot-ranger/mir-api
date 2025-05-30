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


class PostMapUpload(object):
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
        'image_data': 'str',
        'type': 'str',
        'start_map_guid': 'str',
        'start_map_x': 'float',
        'start_map_y': 'float',
        'start_map_theta': 'float',
        'guid': 'str',
        'created_by_id': 'str'
    }

    attribute_map = {
        'image_data': 'image_data',
        'type': 'type',
        'start_map_guid': 'start_map_guid',
        'start_map_x': 'start_map_x',
        'start_map_y': 'start_map_y',
        'start_map_theta': 'start_map_theta',
        'guid': 'guid',
        'created_by_id': 'created_by_id'
    }

    def __init__(self, image_data=None, type=None, start_map_guid=None, start_map_x=None, start_map_y=None, start_map_theta=None, guid=None, created_by_id=None, _configuration=None):  # noqa: E501
        """PostMapUpload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._image_data = None
        self._type = None
        self._start_map_guid = None
        self._start_map_x = None
        self._start_map_y = None
        self._start_map_theta = None
        self._guid = None
        self._created_by_id = None
        self.discriminator = None

        if image_data is not None:
            self.image_data = image_data
        self.type = type
        if start_map_guid is not None:
            self.start_map_guid = start_map_guid
        if start_map_x is not None:
            self.start_map_x = start_map_x
        if start_map_y is not None:
            self.start_map_y = start_map_y
        if start_map_theta is not None:
            self.start_map_theta = start_map_theta
        if guid is not None:
            self.guid = guid
        if created_by_id is not None:
            self.created_by_id = created_by_id

    @property
    def image_data(self):
        """Gets the image_data of this PostMapUpload.  # noqa: E501


        :return: The image_data of this PostMapUpload.  # noqa: E501
        :rtype: str
        """
        return self._image_data

    @image_data.setter
    def image_data(self, image_data):
        """Sets the image_data of this PostMapUpload.


        :param image_data: The image_data of this PostMapUpload.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                image_data is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', image_data)):  # noqa: E501
            raise ValueError(r"Invalid value for `image_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._image_data = image_data

    @property
    def type(self):
        """Gets the type of this PostMapUpload.  # noqa: E501

          # noqa: E501

        :return: The type of this PostMapUpload.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostMapUpload.

          # noqa: E501

        :param type: The type of this PostMapUpload.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def start_map_guid(self):
        """Gets the start_map_guid of this PostMapUpload.  # noqa: E501


        :return: The start_map_guid of this PostMapUpload.  # noqa: E501
        :rtype: str
        """
        return self._start_map_guid

    @start_map_guid.setter
    def start_map_guid(self, start_map_guid):
        """Sets the start_map_guid of this PostMapUpload.


        :param start_map_guid: The start_map_guid of this PostMapUpload.  # noqa: E501
        :type: str
        """

        self._start_map_guid = start_map_guid

    @property
    def start_map_x(self):
        """Gets the start_map_x of this PostMapUpload.  # noqa: E501


        :return: The start_map_x of this PostMapUpload.  # noqa: E501
        :rtype: float
        """
        return self._start_map_x

    @start_map_x.setter
    def start_map_x(self, start_map_x):
        """Sets the start_map_x of this PostMapUpload.


        :param start_map_x: The start_map_x of this PostMapUpload.  # noqa: E501
        :type: float
        """

        self._start_map_x = start_map_x

    @property
    def start_map_y(self):
        """Gets the start_map_y of this PostMapUpload.  # noqa: E501


        :return: The start_map_y of this PostMapUpload.  # noqa: E501
        :rtype: float
        """
        return self._start_map_y

    @start_map_y.setter
    def start_map_y(self, start_map_y):
        """Sets the start_map_y of this PostMapUpload.


        :param start_map_y: The start_map_y of this PostMapUpload.  # noqa: E501
        :type: float
        """

        self._start_map_y = start_map_y

    @property
    def start_map_theta(self):
        """Gets the start_map_theta of this PostMapUpload.  # noqa: E501


        :return: The start_map_theta of this PostMapUpload.  # noqa: E501
        :rtype: float
        """
        return self._start_map_theta

    @start_map_theta.setter
    def start_map_theta(self, start_map_theta):
        """Sets the start_map_theta of this PostMapUpload.


        :param start_map_theta: The start_map_theta of this PostMapUpload.  # noqa: E501
        :type: float
        """

        self._start_map_theta = start_map_theta

    @property
    def guid(self):
        """Gets the guid of this PostMapUpload.  # noqa: E501


        :return: The guid of this PostMapUpload.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this PostMapUpload.


        :param guid: The guid of this PostMapUpload.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def created_by_id(self):
        """Gets the created_by_id of this PostMapUpload.  # noqa: E501


        :return: The created_by_id of this PostMapUpload.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this PostMapUpload.


        :param created_by_id: The created_by_id of this PostMapUpload.  # noqa: E501
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
        if issubclass(PostMapUpload, dict):
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
        if not isinstance(other, PostMapUpload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostMapUpload):
            return True

        return self.to_dict() != other.to_dict()
