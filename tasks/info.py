"""
Module for get/info of sam cli objects
"""

from helper import InvalidInputError, run_command


def get_product_list(org=None):
    """Get list of Products for an org"""
    if org is None:
        raise InvalidInputError('org should be provided to execute this task')
    cmd = 'product list  --org {0}'
    cmd = cmd.format(org)
    run_command(cmd)


def get_provider_list(org=None):
    """Get list of Providers for an org"""
    if org is None:
        raise InvalidInputError('org should be provided to execute this task')
    cmd = 'provider list  --org {0}'
    cmd = cmd.format(org)
    run_command(cmd)


def get_environment_list(org=None):
    """Get list of Environments for an org"""
    if org is None:
        raise InvalidInputError('org should be provided to execute this task')
    cmd = 'environment list  --org {0}'
    cmd = cmd.format(org)
    run_command(cmd)


def run_ping_command():
    """Runs ping command"""
    run_command('ping')


def run_version_command():
    """Runs version command"""
    run_command('version')


def run_about_command():
    """Runs about command"""
    run_command('about')
