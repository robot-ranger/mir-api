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


class GetElevator(object):
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
        'session_guid': 'str',
        'name': 'str',
        'ip': 'str',
        'active': 'bool',
        'turn_in_place': 'bool',
        'one_way': 'int',
        'driver': 'str',
        'port': 'int',
        'elevator_namespace': 'str',
        'username': 'str',
        'password': 'str',
        'authentication': 'str',
        'security_policy': 'str',
        'created_by_id': 'str',
        'created_by': 'str'
    }

    attribute_map = {
        'guid': 'guid',
        'session_guid': 'session_guid',
        'name': 'name',
        'ip': 'ip',
        'active': 'active',
        'turn_in_place': 'turn_in_place',
        'one_way': 'one_way',
        'driver': 'driver',
        'port': 'port',
        'elevator_namespace': 'elevator_namespace',
        'username': 'username',
        'password': 'password',
        'authentication': 'authentication',
        'security_policy': 'security_policy',
        'created_by_id': 'created_by_id',
        'created_by': 'created_by'
    }

    def __init__(self, guid=None, session_guid=None, name=None, ip=None, active=None, turn_in_place=None, one_way=None, driver=None, port=None, elevator_namespace=None, username=None, password=None, authentication=None, security_policy=None, created_by_id=None, created_by=None, _configuration=None):  # noqa: E501
        """GetElevator - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._guid = None
        self._session_guid = None
        self._name = None
        self._ip = None
        self._active = None
        self._turn_in_place = None
        self._one_way = None
        self._driver = None
        self._port = None
        self._elevator_namespace = None
        self._username = None
        self._password = None
        self._authentication = None
        self._security_policy = None
        self._created_by_id = None
        self._created_by = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if session_guid is not None:
            self.session_guid = session_guid
        if name is not None:
            self.name = name
        if ip is not None:
            self.ip = ip
        if active is not None:
            self.active = active
        if turn_in_place is not None:
            self.turn_in_place = turn_in_place
        if one_way is not None:
            self.one_way = one_way
        if driver is not None:
            self.driver = driver
        if port is not None:
            self.port = port
        if elevator_namespace is not None:
            self.elevator_namespace = elevator_namespace
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if authentication is not None:
            self.authentication = authentication
        if security_policy is not None:
            self.security_policy = security_policy
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_by is not None:
            self.created_by = created_by

    @property
    def guid(self):
        """Gets the guid of this GetElevator.  # noqa: E501

        The global id unique across robots that identifies this elevator  # noqa: E501

        :return: The guid of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetElevator.

        The global id unique across robots that identifies this elevator  # noqa: E501

        :param guid: The guid of this GetElevator.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def session_guid(self):
        """Gets the session_guid of this GetElevator.  # noqa: E501

        The global id unique across robots containing this elevator  # noqa: E501

        :return: The session_guid of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._session_guid

    @session_guid.setter
    def session_guid(self, session_guid):
        """Sets the session_guid of this GetElevator.

        The global id unique across robots containing this elevator  # noqa: E501

        :param session_guid: The session_guid of this GetElevator.  # noqa: E501
        :type: str
        """

        self._session_guid = session_guid

    @property
    def name(self):
        """Gets the name of this GetElevator.  # noqa: E501

        The name of the elevator  # noqa: E501

        :return: The name of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetElevator.

        The name of the elevator  # noqa: E501

        :param name: The name of this GetElevator.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ip(self):
        """Gets the ip of this GetElevator.  # noqa: E501

        The ip of the elevator  # noqa: E501

        :return: The ip of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this GetElevator.

        The ip of the elevator  # noqa: E501

        :param ip: The ip of this GetElevator.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def active(self):
        """Gets the active of this GetElevator.  # noqa: E501

        Boolean indicating the state of the elevator  # noqa: E501

        :return: The active of this GetElevator.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this GetElevator.

        Boolean indicating the state of the elevator  # noqa: E501

        :param active: The active of this GetElevator.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def turn_in_place(self):
        """Gets the turn_in_place of this GetElevator.  # noqa: E501

        Boolean indicating if the robot can turn in the elevator  # noqa: E501

        :return: The turn_in_place of this GetElevator.  # noqa: E501
        :rtype: bool
        """
        return self._turn_in_place

    @turn_in_place.setter
    def turn_in_place(self, turn_in_place):
        """Sets the turn_in_place of this GetElevator.

        Boolean indicating if the robot can turn in the elevator  # noqa: E501

        :param turn_in_place: The turn_in_place of this GetElevator.  # noqa: E501
        :type: bool
        """

        self._turn_in_place = turn_in_place

    @property
    def one_way(self):
        """Gets the one_way of this GetElevator.  # noqa: E501

        Integer indicating, if the elevator is one_way only, and in which direction  # noqa: E501

        :return: The one_way of this GetElevator.  # noqa: E501
        :rtype: int
        """
        return self._one_way

    @one_way.setter
    def one_way(self, one_way):
        """Sets the one_way of this GetElevator.

        Integer indicating, if the elevator is one_way only, and in which direction  # noqa: E501

        :param one_way: The one_way of this GetElevator.  # noqa: E501
        :type: int
        """

        self._one_way = one_way

    @property
    def driver(self):
        """Gets the driver of this GetElevator.  # noqa: E501

        Driver used to connect to the elevator server  # noqa: E501

        :return: The driver of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this GetElevator.

        Driver used to connect to the elevator server  # noqa: E501

        :param driver: The driver of this GetElevator.  # noqa: E501
        :type: str
        """

        self._driver = driver

    @property
    def port(self):
        """Gets the port of this GetElevator.  # noqa: E501

        Port on which the serer ir running  # noqa: E501

        :return: The port of this GetElevator.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this GetElevator.

        Port on which the serer ir running  # noqa: E501

        :param port: The port of this GetElevator.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def elevator_namespace(self):
        """Gets the elevator_namespace of this GetElevator.  # noqa: E501

        Namespace under which the elevator is available on the opcua server  # noqa: E501

        :return: The elevator_namespace of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._elevator_namespace

    @elevator_namespace.setter
    def elevator_namespace(self, elevator_namespace):
        """Sets the elevator_namespace of this GetElevator.

        Namespace under which the elevator is available on the opcua server  # noqa: E501

        :param elevator_namespace: The elevator_namespace of this GetElevator.  # noqa: E501
        :type: str
        """

        self._elevator_namespace = elevator_namespace

    @property
    def username(self):
        """Gets the username of this GetElevator.  # noqa: E501

        Username for the opcua server  # noqa: E501

        :return: The username of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GetElevator.

        Username for the opcua server  # noqa: E501

        :param username: The username of this GetElevator.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this GetElevator.  # noqa: E501

        Password for the opcua server  # noqa: E501

        :return: The password of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this GetElevator.

        Password for the opcua server  # noqa: E501

        :param password: The password of this GetElevator.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def authentication(self):
        """Gets the authentication of this GetElevator.  # noqa: E501

        Authentication type for the opcua server  # noqa: E501

        :return: The authentication of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this GetElevator.

        Authentication type for the opcua server  # noqa: E501

        :param authentication: The authentication of this GetElevator.  # noqa: E501
        :type: str
        """

        self._authentication = authentication

    @property
    def security_policy(self):
        """Gets the security_policy of this GetElevator.  # noqa: E501

        Security policy type for the opcua server  # noqa: E501

        :return: The security_policy of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._security_policy

    @security_policy.setter
    def security_policy(self, security_policy):
        """Sets the security_policy of this GetElevator.

        Security policy type for the opcua server  # noqa: E501

        :param security_policy: The security_policy of this GetElevator.  # noqa: E501
        :type: str
        """

        self._security_policy = security_policy

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetElevator.  # noqa: E501

        The global id of the user who created this entry  # noqa: E501

        :return: The created_by_id of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetElevator.

        The global id of the user who created this entry  # noqa: E501

        :param created_by_id: The created_by_id of this GetElevator.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_by(self):
        """Gets the created_by of this GetElevator.  # noqa: E501

        The url to the description of this elevator  # noqa: E501

        :return: The created_by of this GetElevator.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetElevator.

        The url to the description of this elevator  # noqa: E501

        :param created_by: The created_by of this GetElevator.  # noqa: E501
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
        if issubclass(GetElevator, dict):
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
        if not isinstance(other, GetElevator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetElevator):
            return True

        return self.to_dict() != other.to_dict()
