# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_connectivity_updateconnectivityservice_output import TapiConnectivityUpdateconnectivityserviceOutput  # noqa: F401,E501
from tapi_server import util


class TapiConnectivityUpdateConnectivityService(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output=None):  # noqa: E501
        """TapiConnectivityUpdateConnectivityService - a model defined in OpenAPI

        :param output: The output of this TapiConnectivityUpdateConnectivityService.  # noqa: E501
        :type output: TapiConnectivityUpdateconnectivityserviceOutput
        """
        self.openapi_types = {
            'output': TapiConnectivityUpdateconnectivityserviceOutput
        }

        self.attribute_map = {
            'output': 'output'
        }

        self._output = output

    @classmethod
    def from_dict(cls, dikt) -> 'TapiConnectivityUpdateConnectivityService':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.connectivity.UpdateConnectivityService of this TapiConnectivityUpdateConnectivityService.  # noqa: E501
        :rtype: TapiConnectivityUpdateConnectivityService
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output(self):
        """Gets the output of this TapiConnectivityUpdateConnectivityService.


        :return: The output of this TapiConnectivityUpdateConnectivityService.
        :rtype: TapiConnectivityUpdateconnectivityserviceOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TapiConnectivityUpdateConnectivityService.


        :param output: The output of this TapiConnectivityUpdateConnectivityService.
        :type output: TapiConnectivityUpdateconnectivityserviceOutput
        """

        self._output = output