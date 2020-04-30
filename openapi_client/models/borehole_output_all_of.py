# coding: utf-8

"""
    Krak REST API

    Krak REST API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class BoreholeOutputAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'borehole_id': 'int'
    }

    attribute_map = {
        'borehole_id': 'borehole_id'
    }

    def __init__(self, borehole_id=None, local_vars_configuration=None):  # noqa: E501
        """BoreholeOutputAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._borehole_id = None
        self.discriminator = None

        if borehole_id is not None:
            self.borehole_id = borehole_id

    @property
    def borehole_id(self):
        """Gets the borehole_id of this BoreholeOutputAllOf.  # noqa: E501

        Id of the borehole  # noqa: E501

        :return: The borehole_id of this BoreholeOutputAllOf.  # noqa: E501
        :rtype: int
        """
        return self._borehole_id

    @borehole_id.setter
    def borehole_id(self, borehole_id):
        """Sets the borehole_id of this BoreholeOutputAllOf.

        Id of the borehole  # noqa: E501

        :param borehole_id: The borehole_id of this BoreholeOutputAllOf.  # noqa: E501
        :type: int
        """

        self._borehole_id = borehole_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BoreholeOutputAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BoreholeOutputAllOf):
            return True

        return self.to_dict() != other.to_dict()
