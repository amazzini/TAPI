# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_connectivity_getconnectiondetails_output import TapiConnectivityGetconnectiondetailsOutput  # noqa: F401,E501
from tapi_server import util


class TapiConnectivityGetConnectionDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, output=None):  # noqa: E501
        """TapiConnectivityGetConnectionDetails - a model defined in OpenAPI

        :param output: The output of this TapiConnectivityGetConnectionDetails.  # noqa: E501
        :type output: TapiConnectivityGetconnectiondetailsOutput
        """
        self.openapi_types = {
            'output': TapiConnectivityGetconnectiondetailsOutput
        }

        self.attribute_map = {
            'output': 'output'
        }

        self._output = output

    @classmethod
    def from_dict(cls, dikt) -> 'TapiConnectivityGetConnectionDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.connectivity.GetConnectionDetails of this TapiConnectivityGetConnectionDetails.  # noqa: E501
        :rtype: TapiConnectivityGetConnectionDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def output(self):
        """Gets the output of this TapiConnectivityGetConnectionDetails.


        :return: The output of this TapiConnectivityGetConnectionDetails.
        :rtype: TapiConnectivityGetconnectiondetailsOutput
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this TapiConnectivityGetConnectionDetails.


        :param output: The output of this TapiConnectivityGetConnectionDetails.
        :type output: TapiConnectivityGetconnectiondetailsOutput
        """

        self._output = output