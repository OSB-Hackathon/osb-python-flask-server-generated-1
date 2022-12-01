# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ServiceBindingMetadata(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, expires_at: str=None, renew_before: str=None):  # noqa: E501
        """ServiceBindingMetadata - a model defined in Swagger

        :param expires_at: The expires_at of this ServiceBindingMetadata.  # noqa: E501
        :type expires_at: str
        :param renew_before: The renew_before of this ServiceBindingMetadata.  # noqa: E501
        :type renew_before: str
        """
        self.swagger_types = {
            'expires_at': str,
            'renew_before': str
        }

        self.attribute_map = {
            'expires_at': 'expires_at',
            'renew_before': 'renew_before'
        }

        self._expires_at = expires_at
        self._renew_before = renew_before

    @classmethod
    def from_dict(cls, dikt) -> 'ServiceBindingMetadata':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServiceBindingMetadata of this ServiceBindingMetadata.  # noqa: E501
        :rtype: ServiceBindingMetadata
        """
        return util.deserialize_model(dikt, cls)

    @property
    def expires_at(self) -> str:
        """Gets the expires_at of this ServiceBindingMetadata.


        :return: The expires_at of this ServiceBindingMetadata.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at: str):
        """Sets the expires_at of this ServiceBindingMetadata.


        :param expires_at: The expires_at of this ServiceBindingMetadata.
        :type expires_at: str
        """

        self._expires_at = expires_at

    @property
    def renew_before(self) -> str:
        """Gets the renew_before of this ServiceBindingMetadata.


        :return: The renew_before of this ServiceBindingMetadata.
        :rtype: str
        """
        return self._renew_before

    @renew_before.setter
    def renew_before(self, renew_before: str):
        """Sets the renew_before of this ServiceBindingMetadata.


        :param renew_before: The renew_before of this ServiceBindingMetadata.
        :type renew_before: str
        """

        self._renew_before = renew_before
