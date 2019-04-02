# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rapid7vmconsole.models.link import Link  # noqa: F401,E501
from rapid7vmconsole.models.vulnerabilities import Vulnerabilities  # noqa: F401,E501


class Scan(object):
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
        'assets': 'int',
        'duration': 'str',
        'end_time': 'str',
        'engine_id': 'int',
        'engine_name': 'str',
        'id': 'int',
        'links': 'list[Link]',
        'message': 'str',
        'scan_name': 'str',
        'scan_type': 'str',
        'start_time': 'str',
        'started_by': 'str',
        'status': 'str',
        'vulnerabilities': 'Vulnerabilities'
    }

    attribute_map = {
        'assets': 'assets',
        'duration': 'duration',
        'end_time': 'endTime',
        'engine_id': 'engineId',
        'engine_name': 'engineName',
        'id': 'id',
        'links': 'links',
        'message': 'message',
        'scan_name': 'scanName',
        'scan_type': 'scanType',
        'start_time': 'startTime',
        'started_by': 'startedBy',
        'status': 'status',
        'vulnerabilities': 'vulnerabilities'
    }

    def __init__(self, assets=None, duration=None, end_time=None, engine_id=None, engine_name=None, id=None, links=None, message=None, scan_name=None, scan_type=None, start_time=None, started_by=None, status=None, vulnerabilities=None):  # noqa: E501
        """Scan - a model defined in Swagger"""  # noqa: E501

        self._assets = None
        self._duration = None
        self._end_time = None
        self._engine_id = None
        self._engine_name = None
        self._id = None
        self._links = None
        self._message = None
        self._scan_name = None
        self._scan_type = None
        self._start_time = None
        self._started_by = None
        self._status = None
        self._vulnerabilities = None
        self.discriminator = None

        if assets is not None:
            self.assets = assets
        if duration is not None:
            self.duration = duration
        if end_time is not None:
            self.end_time = end_time
        if engine_id is not None:
            self.engine_id = engine_id
        if engine_name is not None:
            self.engine_name = engine_name
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if message is not None:
            self.message = message
        if scan_name is not None:
            self.scan_name = scan_name
        if scan_type is not None:
            self.scan_type = scan_type
        if start_time is not None:
            self.start_time = start_time
        if started_by is not None:
            self.started_by = started_by
        if status is not None:
            self.status = status
        if vulnerabilities is not None:
            self.vulnerabilities = vulnerabilities

    @property
    def assets(self):
        """Gets the assets of this Scan.  # noqa: E501

        The number of assets found in the scan.  # noqa: E501

        :return: The assets of this Scan.  # noqa: E501
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this Scan.

        The number of assets found in the scan.  # noqa: E501

        :param assets: The assets of this Scan.  # noqa: E501
        :type: int
        """

        self._assets = assets

    @property
    def duration(self):
        """Gets the duration of this Scan.  # noqa: E501

        The duration of the scan in ISO8601 format.  # noqa: E501

        :return: The duration of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Scan.

        The duration of the scan in ISO8601 format.  # noqa: E501

        :param duration: The duration of this Scan.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def end_time(self):
        """Gets the end_time of this Scan.  # noqa: E501

        The end time of the scan in ISO8601 format.  # noqa: E501

        :return: The end_time of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Scan.

        The end time of the scan in ISO8601 format.  # noqa: E501

        :param end_time: The end_time of this Scan.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def engine_id(self):
        """Gets the engine_id of this Scan.  # noqa: E501

        The identifier of the scan engine.  # noqa: E501

        :return: The engine_id of this Scan.  # noqa: E501
        :rtype: int
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        """Sets the engine_id of this Scan.

        The identifier of the scan engine.  # noqa: E501

        :param engine_id: The engine_id of this Scan.  # noqa: E501
        :type: int
        """

        self._engine_id = engine_id

    @property
    def engine_name(self):
        """Gets the engine_name of this Scan.  # noqa: E501

        The name of the scan engine.  # noqa: E501

        :return: The engine_name of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this Scan.

        The name of the scan engine.  # noqa: E501

        :param engine_name: The engine_name of this Scan.  # noqa: E501
        :type: str
        """

        self._engine_name = engine_name

    @property
    def id(self):
        """Gets the id of this Scan.  # noqa: E501

        The identifier of the scan.  # noqa: E501

        :return: The id of this Scan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Scan.

        The identifier of the scan.  # noqa: E501

        :param id: The id of this Scan.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this Scan.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this Scan.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Scan.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this Scan.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def message(self):
        """Gets the message of this Scan.  # noqa: E501

        The reason for the scan status.  # noqa: E501

        :return: The message of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Scan.

        The reason for the scan status.  # noqa: E501

        :param message: The message of this Scan.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def scan_name(self):
        """Gets the scan_name of this Scan.  # noqa: E501

        The user-driven scan name for the scan.  # noqa: E501

        :return: The scan_name of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._scan_name

    @scan_name.setter
    def scan_name(self, scan_name):
        """Sets the scan_name of this Scan.

        The user-driven scan name for the scan.  # noqa: E501

        :param scan_name: The scan_name of this Scan.  # noqa: E501
        :type: str
        """

        self._scan_name = scan_name

    @property
    def scan_type(self):
        """Gets the scan_type of this Scan.  # noqa: E501

        The scan type (automated, manual, scheduled).   # noqa: E501

        :return: The scan_type of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        """Sets the scan_type of this Scan.

        The scan type (automated, manual, scheduled).   # noqa: E501

        :param scan_type: The scan_type of this Scan.  # noqa: E501
        :type: str
        """

        self._scan_type = scan_type

    @property
    def start_time(self):
        """Gets the start_time of this Scan.  # noqa: E501

        The start time of the scan in ISO8601 format.  # noqa: E501

        :return: The start_time of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Scan.

        The start time of the scan in ISO8601 format.  # noqa: E501

        :param start_time: The start_time of this Scan.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def started_by(self):
        """Gets the started_by of this Scan.  # noqa: E501

        The name of the user that started the scan.  # noqa: E501

        :return: The started_by of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._started_by

    @started_by.setter
    def started_by(self, started_by):
        """Sets the started_by of this Scan.

        The name of the user that started the scan.  # noqa: E501

        :param started_by: The started_by of this Scan.  # noqa: E501
        :type: str
        """

        self._started_by = started_by

    @property
    def status(self):
        """Gets the status of this Scan.  # noqa: E501

        The scan status.  # noqa: E501

        :return: The status of this Scan.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Scan.

        The scan status.  # noqa: E501

        :param status: The status of this Scan.  # noqa: E501
        :type: str
        """
        allowed_values = ["aborted", "unknown", "running", "finished", "stopped", "error", "paused", "dispatched", "integrating"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def vulnerabilities(self):
        """Gets the vulnerabilities of this Scan.  # noqa: E501

        The vulnerability synopsis of the scan.  # noqa: E501

        :return: The vulnerabilities of this Scan.  # noqa: E501
        :rtype: Vulnerabilities
        """
        return self._vulnerabilities

    @vulnerabilities.setter
    def vulnerabilities(self, vulnerabilities):
        """Sets the vulnerabilities of this Scan.

        The vulnerability synopsis of the scan.  # noqa: E501

        :param vulnerabilities: The vulnerabilities of this Scan.  # noqa: E501
        :type: Vulnerabilities
        """

        self._vulnerabilities = vulnerabilities

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
        if issubclass(Scan, dict):
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
        if not isinstance(other, Scan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other