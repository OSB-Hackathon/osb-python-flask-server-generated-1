# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MaintenanceInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, version: str=None, description: str=None):  # noqa: E501
        """MaintenanceInfo - a model defined in Swagger

        :param version: The version of this MaintenanceInfo.  # noqa: E501
        :type version: str
        :param description: The description of this MaintenanceInfo.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'version': str,
            'description': str
        }

        self.attribute_map = {
            'version': 'version',
            'description': 'description'
        }

        self._version = version
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'MaintenanceInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MaintenanceInfo of this MaintenanceInfo.  # noqa: E501
        :rtype: MaintenanceInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def version(self) -> str:
        """Gets the version of this MaintenanceInfo.


        :return: The version of this MaintenanceInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this MaintenanceInfo.


        :param version: The version of this MaintenanceInfo.
        :type version: str
        """

        self._version = version

    @property
    def description(self) -> str:
        """Gets the description of this MaintenanceInfo.


        :return: The description of this MaintenanceInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this MaintenanceInfo.


        :param description: The description of this MaintenanceInfo.
        :type description: str
        """

        self._description = description
