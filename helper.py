"""
Python Module for sam tests
"""

import ConfigParser
from fabric.api import run

USER_NAME = 'admin'
USER_PASSWORD = 'admin'

CONF = ConfigParser.RawConfigParser()
# if the config file is not found, it will be silently ignored
CONF.read('samtools.properties')


class InvalidInputError(Exception):
    """Indicates an invalid input error"""
    # pylint: disable=W0703


def run_command(cmd=None, quiet=False, warn_only=False):
    """Executes the actual command"""
    basic_cmd = 'headpin -u {0} -p {1} '.format(USER_NAME, USER_PASSWORD)
    if cmd is not None:
        basic_cmd = basic_cmd + cmd
    return run('%s' % basic_cmd, quiet=quiet, warn_only=warn_only)


def get_host(input_list):
    """Reads the config file and appends the host to the fabric host list"""
    try:
        host = CONF.get('main', 'host')
        if host is not None:
            input_list.append(host)
            print input_list
    except ConfigParser.NoSectionError:
        # No need to do anything. Just ignore the exception
        pass
    return input_list


def get_test_username(input_user):
    """Fabric user will be overridden by the user specified in config file """
    try:
        user = CONF.get('main', 'user')
        if user is not '' or user is not None:
            input_user = user
    except ConfigParser.NoSectionError:
        # No need to do anything. Just ignore the exception
        pass
    return input_user


def get_config(section, key):
    """Returns the value if present in the config"""
    value = None
    try:
        value = CONF.get(section, key)
    except ConfigParser.NoSectionError:
        # No need to do anything. Just ignore the exception
        pass
    return value
