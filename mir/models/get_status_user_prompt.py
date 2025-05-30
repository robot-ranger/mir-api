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


class GetStatusUserPrompt(object):
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
        'user_group': 'str',
        'question': 'str',
        'timeout': 'float',
        'options': 'list[str]'
    }

    attribute_map = {
        'guid': 'guid',
        'user_group': 'user_group',
        'question': 'question',
        'timeout': 'timeout',
        'options': 'options'
    }

    def __init__(self, guid=None, user_group=None, question=None, timeout=None, options=None, _configuration=None):  # noqa: E501
        """GetStatusUserPrompt - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._guid = None
        self._user_group = None
        self._question = None
        self._timeout = None
        self._options = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if user_group is not None:
            self.user_group = user_group
        if question is not None:
            self.question = question
        if timeout is not None:
            self.timeout = timeout
        if options is not None:
            self.options = options

    @property
    def guid(self):
        """Gets the guid of this GetStatusUserPrompt.  # noqa: E501

          # noqa: E501

        :return: The guid of this GetStatusUserPrompt.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this GetStatusUserPrompt.

          # noqa: E501

        :param guid: The guid of this GetStatusUserPrompt.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def user_group(self):
        """Gets the user_group of this GetStatusUserPrompt.  # noqa: E501

          # noqa: E501

        :return: The user_group of this GetStatusUserPrompt.  # noqa: E501
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this GetStatusUserPrompt.

          # noqa: E501

        :param user_group: The user_group of this GetStatusUserPrompt.  # noqa: E501
        :type: str
        """

        self._user_group = user_group

    @property
    def question(self):
        """Gets the question of this GetStatusUserPrompt.  # noqa: E501

          # noqa: E501

        :return: The question of this GetStatusUserPrompt.  # noqa: E501
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this GetStatusUserPrompt.

          # noqa: E501

        :param question: The question of this GetStatusUserPrompt.  # noqa: E501
        :type: str
        """

        self._question = question

    @property
    def timeout(self):
        """Gets the timeout of this GetStatusUserPrompt.  # noqa: E501

          # noqa: E501

        :return: The timeout of this GetStatusUserPrompt.  # noqa: E501
        :rtype: float
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this GetStatusUserPrompt.

          # noqa: E501

        :param timeout: The timeout of this GetStatusUserPrompt.  # noqa: E501
        :type: float
        """

        self._timeout = timeout

    @property
    def options(self):
        """Gets the options of this GetStatusUserPrompt.  # noqa: E501

          # noqa: E501

        :return: The options of this GetStatusUserPrompt.  # noqa: E501
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this GetStatusUserPrompt.

          # noqa: E501

        :param options: The options of this GetStatusUserPrompt.  # noqa: E501
        :type: list[str]
        """

        self._options = options

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
        if issubclass(GetStatusUserPrompt, dict):
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
        if not isinstance(other, GetStatusUserPrompt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetStatusUserPrompt):
            return True

        return self.to_dict() != other.to_dict()
