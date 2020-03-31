# pylint: disable=trailing-newlines
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=unused-import
# pylint: disable=invalid-name

r"""
Copyright &copy; 2020 NetApp Inc.
All rights reserved.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema


__all__ = ["OracleOnNfsOraHomeStorageService", "OracleOnNfsOraHomeStorageServiceSchema"]
__pdoc__ = {
    "OracleOnNfsOraHomeStorageServiceSchema.resource": False,
    "OracleOnNfsOraHomeStorageService": False,
}


class OracleOnNfsOraHomeStorageServiceSchema(ResourceSchema):
    """The fields of the OracleOnNfsOraHomeStorageService object"""

    name = fields.Str(data_key="name")
    r""" The storage service of the ORACLE_HOME storage volume.

Valid choices:

* extreme
* performance
* value """

    @property
    def resource(self):
        return OracleOnNfsOraHomeStorageService

    @property
    def patchable_fields(self):
        return [
            "name",
        ]

    @property
    def postable_fields(self):
        return [
            "name",
        ]


class OracleOnNfsOraHomeStorageService(Resource):  # pylint: disable=missing-docstring

    _schema = OracleOnNfsOraHomeStorageServiceSchema
