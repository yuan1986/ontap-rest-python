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


__all__ = ["CifsTarget", "CifsTargetSchema"]
__pdoc__ = {
    "CifsTargetSchema.resource": False,
    "CifsTarget": False,
}


class CifsTargetSchema(ResourceSchema):
    """The fields of the CifsTarget object"""

    home_directory = fields.Boolean(data_key="home_directory")
    r""" Specify if the destination share is a home directory. """

    locality = fields.Str(data_key="locality")
    r""" Specifies whether the CIFS symbolic link is a local link or wide link.
The following values are supported:

* local - Local symbolic link maps only to the same CIFS share.
* widelink - Wide symbolic link maps to any CIFS share on the network.


Valid choices:

* local
* widelink """

    path = fields.Str(data_key="path")
    r""" Specifies the CIFS path on the destination to which the symbolic link maps. The final path is generated by concatenating the CIFS server name, the share name, the cifs-path and the remaining path in the symbolic link left after the prefix match. This value is specified by using a UNIX-style path name. The trailing forward slash is required for the full path name to be properly interpreted.

Example: /dir1/dir2/ """

    server = fields.Str(data_key="server")
    r""" Specifies the destination CIFS server where the
UNIX symbolic link is pointing. This field is mandatory if the
locality of the symbolic link is 'widelink'.
You can specify the value in any of the following formats:

  * DNS name of the CIFS server.
  * IP address of the CIFS server.
  * NetBIOS name of the CIFS server.


Example: ENGCIFS """

    share = fields.Str(data_key="share")
    r""" Specifies the CIFS share name on the destination CIFS server to which the UNIX symbolic link is pointing.

Example: ENG_SHARE """

    @property
    def resource(self):
        return CifsTarget

    @property
    def patchable_fields(self):
        return [
            "home_directory",
            "locality",
            "path",
            "server",
            "share",
        ]

    @property
    def postable_fields(self):
        return [
            "home_directory",
            "locality",
            "path",
            "server",
            "share",
        ]


class CifsTarget(Resource):  # pylint: disable=missing-docstring

    _schema = CifsTargetSchema
