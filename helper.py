"""
Python Module for sam tests
"""

from fabric.api import run

USER_NAME = 'admin'
USER_PASSWORD = 'admin'


class InvalidInputError(Exception):
    """Indicates an invalid input error"""


def run_command(cmd=None, quiet=False, warn_only=False):
    """Executes the actual command"""
    basic_cmd = 'headpin -u {0} -p {1} '.format(USER_NAME, USER_PASSWORD)
    if cmd is not None:
        basic_cmd = basic_cmd + cmd
    return run('%s' % basic_cmd, quiet=quiet, warn_only=warn_only)
