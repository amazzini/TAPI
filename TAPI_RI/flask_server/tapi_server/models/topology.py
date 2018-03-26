# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.link import Link  # noqa: F401,E501
from tapi_server.models.name_and_value import NameAndValue  # noqa: F401,E501
from tapi_server.models.node import Node  # noqa: F401,E501
from tapi_server.models.resource_spec import ResourceSpec  # noqa: F401,E501
from tapi_server import util


class Topology(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uuid: str=None, name: List[NameAndValue]=None, node: List[Node]=None, link: List[Link]=None, layer_protocol_name: List[str]=None):  # noqa: E501
        """Topology - a model defined in Swagger

        :param uuid: The uuid of this Topology.  # noqa: E501
        :type uuid: str
        :param name: The name of this Topology.  # noqa: E501
        :type name: List[NameAndValue]
        :param node: The node of this Topology.  # noqa: E501
        :type node: List[Node]
        :param link: The link of this Topology.  # noqa: E501
        :type link: List[Link]
        :param layer_protocol_name: The layer_protocol_name of this Topology.  # noqa: E501
        :type layer_protocol_name: List[str]
        """
        self.swagger_types = {
            'uuid': str,
            'name': List[NameAndValue],
            'node': List[Node],
            'link': List[Link],
            'layer_protocol_name': List[str]
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'name': 'name',
            'node': 'node',
            'link': 'link',
            'layer_protocol_name': 'layer-protocol-name'
        }

        self._uuid = uuid
        self._name = name
        self._node = node
        self._link = link
        self._layer_protocol_name = layer_protocol_name

    @classmethod
    def from_dict(cls, dikt) -> 'Topology':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The topology of this Topology.  # noqa: E501
        :rtype: Topology
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uuid(self) -> str:
        """Gets the uuid of this Topology.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :return: The uuid of this Topology.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this Topology.

        UUID: An identifier that is universally unique within an identifier space, where the identifier space is itself globally unique, and immutable. An UUID carries no semantics with respect to the purpose or state of the entity. UUID here uses string representation as defined in RFC 4122.  The canonical representation uses lowercase characters. Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-' + '[0-9a-fA-F]{4}-[0-9a-fA-F]{12}  Example of a UUID in string representation: f81d4fae-7dec-11d0-a765-00a0c91e6bf6  # noqa: E501

        :param uuid: The uuid of this Topology.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def name(self) -> List[NameAndValue]:
        """Gets the name of this Topology.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this Topology.
        :rtype: List[NameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name: List[NameAndValue]):
        """Sets the name of this Topology.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this Topology.
        :type name: List[NameAndValue]
        """

        self._name = name

    @property
    def node(self) -> List[Node]:
        """Gets the node of this Topology.


        :return: The node of this Topology.
        :rtype: List[Node]
        """
        return self._node

    @node.setter
    def node(self, node: List[Node]):
        """Sets the node of this Topology.


        :param node: The node of this Topology.
        :type node: List[Node]
        """

        self._node = node

    @property
    def link(self) -> List[Link]:
        """Gets the link of this Topology.


        :return: The link of this Topology.
        :rtype: List[Link]
        """
        return self._link

    @link.setter
    def link(self, link: List[Link]):
        """Sets the link of this Topology.


        :param link: The link of this Topology.
        :type link: List[Link]
        """

        self._link = link

    @property
    def layer_protocol_name(self) -> List[str]:
        """Gets the layer_protocol_name of this Topology.


        :return: The layer_protocol_name of this Topology.
        :rtype: List[str]
        """
        return self._layer_protocol_name

    @layer_protocol_name.setter
    def layer_protocol_name(self, layer_protocol_name: List[str]):
        """Sets the layer_protocol_name of this Topology.


        :param layer_protocol_name: The layer_protocol_name of this Topology.
        :type layer_protocol_name: List[str]
        """
        allowed_values = ["OTSiA", "OCH", "OTU", "ODU", "ETH", "ETY", "DSR"]  # noqa: E501
        if not set(layer_protocol_name).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `layer_protocol_name` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(layer_protocol_name) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._layer_protocol_name = layer_protocol_name