"""
Module for manipulation of sam manifests
"""

from helper import InvalidInputError, run_command
from tasks.create import create_org

MANIFEST_URL = "/tmp/test_sam_manifest.zip"
PROVIDER_NAME = "Red Hat"


def import_manifest(org=None, filepath=None, deleted=True):
    """Imports a manifest

    If delete is set to False, the manifest will not be deleted and the user
    has to handle the deletion manually or by calling delete_manifest

    """
    if org is None:
        org = create_org()
    if filepath is None:
        filepath = MANIFEST_URL
    cmd = ('provider import_manifest create --name "{0}" --org {1} '
           '--file "{2}"').format(PROVIDER_NAME, org, filepath)
    run_command(cmd)
    if deleted is True:
        print ('* After manifest import, manifest will be deleted so as '
               'to reuse it *')
        delete_manifest(org)


def refresh_manifest(org=None):
    """Refreshes a manifest"""
    if org is None:
        raise InvalidInputError('org should be provided to execute this task')
    cmd = ('provider refresh_manifest --name "{0}" '
           '--org {1}'.format(PROVIDER_NAME, org))
    run_command(cmd)


def delete_manifest(org=None):
    """Deletes a manifest"""
    if org is None:
        raise InvalidInputError('org should be provided to execute this task')
    cmd = ('provider delete_manifest --name "{0}" '
           '--org {1}'.format(PROVIDER_NAME, org))
    run_command(cmd)
