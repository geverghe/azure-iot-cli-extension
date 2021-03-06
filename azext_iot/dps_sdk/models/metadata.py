# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Metadata(Model):
    """Metadata.

    :param last_updated:
    :type last_updated: datetime
    :param last_updated_version: This SHOULD be null for Reported properties
     metadata and MUST not be null for Desired properties metadata.
    :type last_updated_version: long
    """

    _attribute_map = {
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'last_updated_version': {'key': 'lastUpdatedVersion', 'type': 'long'},
    }

    def __init__(self, last_updated=None, last_updated_version=None):
        super(Metadata, self).__init__()
        self.last_updated = last_updated
        self.last_updated_version = last_updated_version
