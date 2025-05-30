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


class PostPaths(object):
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
        'start_pos_id': 'str',
        'goal_pos_id': 'str',
        'length': 'float',
        'time': 'float',
        'path': 'str',
        'footprint': 'str',
        'map_crc': 'str',
        'last_used': 'datetime',
        'autogenerated': 'bool',
        'valid': 'bool'
    }

    attribute_map = {
        'guid': 'guid',
        'start_pos_id': 'start_pos_id',
        'goal_pos_id': 'goal_pos_id',
        'length': 'length',
        'time': 'time',
        'path': 'path',
        'footprint': 'footprint',
        'map_crc': 'map_crc',
        'last_used': 'last_used',
        'autogenerated': 'autogenerated',
        'valid': 'valid'
    }

    def __init__(self, guid=None, start_pos_id=None, goal_pos_id=None, length=None, time=None, path=None, footprint=None, map_crc=None, last_used=None, autogenerated=None, valid=None, _configuration=None):  # noqa: E501
        """PostPaths - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._guid = None
        self._start_pos_id = None
        self._goal_pos_id = None
        self._length = None
        self._time = None
        self._path = None
        self._footprint = None
        self._map_crc = None
        self._last_used = None
        self._autogenerated = None
        self._valid = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        self.start_pos_id = start_pos_id
        self.goal_pos_id = goal_pos_id
        self.length = length
        self.time = time
        self.path = path
        self.footprint = footprint
        self.map_crc = map_crc
        self.last_used = last_used
        self.autogenerated = autogenerated
        self.valid = valid

    @property
    def guid(self):
        """Gets the guid of this PostPaths.  # noqa: E501


        :return: The guid of this PostPaths.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this PostPaths.


        :param guid: The guid of this PostPaths.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def start_pos_id(self):
        """Gets the start_pos_id of this PostPaths.  # noqa: E501


        :return: The start_pos_id of this PostPaths.  # noqa: E501
        :rtype: str
        """
        return self._start_pos_id

    @start_pos_id.setter
    def start_pos_id(self, start_pos_id):
        """Sets the start_pos_id of this PostPaths.


        :param start_pos_id: The start_pos_id of this PostPaths.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and start_pos_id is None:
            raise ValueError("Invalid value for `start_pos_id`, must not be `None`")  # noqa: E501

        self._start_pos_id = start_pos_id

    @property
    def goal_pos_id(self):
        """Gets the goal_pos_id of this PostPaths.  # noqa: E501


        :return: The goal_pos_id of this PostPaths.  # noqa: E501
        :rtype: str
        """
        return self._goal_pos_id

    @goal_pos_id.setter
    def goal_pos_id(self, goal_pos_id):
        """Sets the goal_pos_id of this PostPaths.


        :param goal_pos_id: The goal_pos_id of this PostPaths.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and goal_pos_id is None:
            raise ValueError("Invalid value for `goal_pos_id`, must not be `None`")  # noqa: E501

        self._goal_pos_id = goal_pos_id

    @property
    def length(self):
        """Gets the length of this PostPaths.  # noqa: E501


        :return: The length of this PostPaths.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this PostPaths.


        :param length: The length of this PostPaths.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def time(self):
        """Gets the time of this PostPaths.  # noqa: E501


        :return: The time of this PostPaths.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this PostPaths.


        :param time: The time of this PostPaths.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def path(self):
        """Gets the path of this PostPaths.  # noqa: E501


        :return: The path of this PostPaths.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PostPaths.


        :param path: The path of this PostPaths.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                path is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', path)):  # noqa: E501
            raise ValueError(r"Invalid value for `path`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._path = path

    @property
    def footprint(self):
        """Gets the footprint of this PostPaths.  # noqa: E501

        Max length: 255  # noqa: E501

        :return: The footprint of this PostPaths.  # noqa: E501
        :rtype: str
        """
        return self._footprint

    @footprint.setter
    def footprint(self, footprint):
        """Sets the footprint of this PostPaths.

        Max length: 255  # noqa: E501

        :param footprint: The footprint of this PostPaths.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and footprint is None:
            raise ValueError("Invalid value for `footprint`, must not be `None`")  # noqa: E501

        self._footprint = footprint

    @property
    def map_crc(self):
        """Gets the map_crc of this PostPaths.  # noqa: E501

        Min length: 32, Max length: 32  # noqa: E501

        :return: The map_crc of this PostPaths.  # noqa: E501
        :rtype: str
        """
        return self._map_crc

    @map_crc.setter
    def map_crc(self, map_crc):
        """Sets the map_crc of this PostPaths.

        Min length: 32, Max length: 32  # noqa: E501

        :param map_crc: The map_crc of this PostPaths.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and map_crc is None:
            raise ValueError("Invalid value for `map_crc`, must not be `None`")  # noqa: E501

        self._map_crc = map_crc

    @property
    def last_used(self):
        """Gets the last_used of this PostPaths.  # noqa: E501


        :return: The last_used of this PostPaths.  # noqa: E501
        :rtype: datetime
        """
        return self._last_used

    @last_used.setter
    def last_used(self, last_used):
        """Sets the last_used of this PostPaths.


        :param last_used: The last_used of this PostPaths.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and last_used is None:
            raise ValueError("Invalid value for `last_used`, must not be `None`")  # noqa: E501

        self._last_used = last_used

    @property
    def autogenerated(self):
        """Gets the autogenerated of this PostPaths.  # noqa: E501


        :return: The autogenerated of this PostPaths.  # noqa: E501
        :rtype: bool
        """
        return self._autogenerated

    @autogenerated.setter
    def autogenerated(self, autogenerated):
        """Sets the autogenerated of this PostPaths.


        :param autogenerated: The autogenerated of this PostPaths.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and autogenerated is None:
            raise ValueError("Invalid value for `autogenerated`, must not be `None`")  # noqa: E501

        self._autogenerated = autogenerated

    @property
    def valid(self):
        """Gets the valid of this PostPaths.  # noqa: E501


        :return: The valid of this PostPaths.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this PostPaths.


        :param valid: The valid of this PostPaths.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and valid is None:
            raise ValueError("Invalid value for `valid`, must not be `None`")  # noqa: E501

        self._valid = valid

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
        if issubclass(PostPaths, dict):
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
        if not isinstance(other, PostPaths):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostPaths):
            return True

        return self.to_dict() != other.to_dict()
