"""
Module for get/info of sam cli objects
"""

from helper import InvalidInputError, run_command


def get_product_list(org=None):
    """Get list of Products for an org"""
    if org is None:
        raise InvalidInputError('org should be provided to execute this task')
    cmd = 'product list  --org {0}'.format(org)
    run_command(cmd)


def get_provider_list(org=None):
    """Get list of Providers for an org"""
    if org is None:
        raise InvalidInputError('org should be provided to execute this task')
    cmd = 'provider list  --org {0}'.format(org)
    run_command(cmd)


def get_environment_list(org=None):
    """Get list of Environments for an org"""
    if org is None:
        raise InvalidInputError('org should be provided to execute this task')
    cmd = 'environment list  --org {0}'.format(org)
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


def get_org(name):
    """Gets an org"""
    if name is None:
        raise InvalidInputError('name should be provided to execute this task')
    cmd = 'org info  --name {0}'.format(name)
    run_command(cmd)


def get_activation_key(name, org):
    """Gets an activation key"""
    if name is None or org is None:
        raise InvalidInputError('name and org should be provided to '
                                'execute this task')
    cmd = 'activation_key info  --name {0} --org {1}'.format(name, org)
    run_command(cmd)


def get_user(username):
    """Gets an user"""
    if username is None:
        raise InvalidInputError('username should be provided to '
                                'execute this task')
    cmd = 'user info  --username {0}'.format(username)
    run_command(cmd)


def get_role(name):
    """Gets a role"""
    if name is None:
        raise InvalidInputError('role name should be provided to '
                                'execute this task')
    cmd = 'user_role info  --name {0}'.format(name)
    run_command(cmd)


def get_permission(user_role):
    """Gets a permission"""
    if user_role is None:
        raise InvalidInputError('user_rold should be provided to '
                                'execute this task')
    cmd = 'permission list  --user_role {0}'.format(user_role)
    run_command(cmd)


def get_distributor(name, org):
    """Gets a distributor"""
    if name is None or org is None:
        raise InvalidInputError('name and org should be provided to '
                                'execute this task')
    cmd = 'distributor info --name {0} --org {1}'.format(name, org)
    run_command(cmd)


def get_system(name, org):
    """Gets a system"""
    if name is None or org is None:
        raise InvalidInputError('name and org should be provided to '
                                'execute this task')
    cmd = 'system info --name {0} --org {1}'.format(name, org)
    # Open bug
    run_command(cmd, warn_only=True)


def get_system_group(name, org):
    """Gets a system group"""
    if name is None or org is None:
        raise InvalidInputError('name and org should be provided to '
                                'execute this task')
    cmd = 'system_group info --name {0} --org {1}'.format(name, org)
    run_command(cmd)
