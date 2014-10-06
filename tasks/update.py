"""
Module for creation of sam cli objects
"""

from helper import InvalidInputError, run_command


def update_org(name, new_description=None):
    """Updates an org."""
    if name is None:
        raise InvalidInputError('org name should be provided'
                                'to execute this task')
    run_command('org update --name={0} --description={1}'.format(
                name, new_description))
    return name


def update_activation_key(name, org, new_name=None, new_description=None,
                          new_limit=None):
    """Updates an activation key."""
    if name is None or org is None:
        raise InvalidInputError('Activation key name and org name should be '
                                'provided to execute this task')
    cmd = 'activation_key update --name {0} --org {1} '.format(name, org)
    if new_name is not None:
        cmd = cmd + '--new_name={0} '.format(new_name)
    if new_name is not None:
        cmd = cmd + '--description={0} '.format(new_description)
    if new_name is not None:
        cmd = cmd + '--limit={0}'.format(new_limit)
    run_command(cmd)
    if new_name is not None:
        return new_name


def update_user(username, new_password=None, new_email=None,
                new_default_organization=None, new_default_locale=None):
    """Updates an user"""
    if username is None:
        raise InvalidInputError('username should be provided to '
                                'execute this task')
    cmd = 'user update --username {0} '.format(username)
    if new_password is not None:
        cmd = cmd + ' --password {0} '.format(new_password)
    if new_email is not None:
        cmd = cmd + ' --email {0} '.format(new_email)
    if new_default_organization is not None:
        cmd = cmd + (' --default_organization'
                     ' {0} '.format(new_default_organization))
    if new_default_locale is not None:
        cmd = cmd + ' --default_locale {0}'.format(new_default_locale)
    run_command(cmd)
    return username


def update_role(name, new_name=None, new_description=None):
    """Updates an user role"""
    if name is None:
        raise InvalidInputError('role name should be provided to '
                                'execute this task')
    cmd = 'user_role update --name {0} '.format(name)
    if new_name is not None:
        cmd = cmd + ' --new_name {0} '.format(new_name)
    if new_description is not None:
        cmd = cmd + ' --description {0} '.format(new_description)
    run_command(cmd)
    if new_name is not None:
        return new_name


def update_distributor(name, org, new_name=None, new_description=None):
    """Updates a distributor"""
    if name is None or org is None:
        raise InvalidInputError('name and org should be provided to '
                                'execute this task')
    cmd = 'distributor update --name {0} --org {1} '.format(name, org)
    if new_name is not None:
        cmd = cmd + '--new_name {0} '.format(new_name)
    if new_description is not None:
        cmd = cmd + '--description {0}'.format(new_description)
    run_command(cmd)
    if new_name is not None:
        return new_name


def update_system(name=None, org=None, new_name=None, new_description=None):
    """Updates a system"""
    if name is None or org is None:
        raise InvalidInputError('name and org should be provided to '
                                'execute this task')
    cmd = 'system update --name {0} --org {1} '.format(name, org)
    if new_name is not None:
        cmd = cmd + '--new_name {0} '.format(new_name)
    if new_description is not None:
        cmd = cmd + '--description {0}'.format(new_description)
    run_command(cmd, warn_only=True)
    if new_name is not None:
        return new_name


def update_system_group(name=None, org=None,
                        new_name=None, new_description=None,
                        new_max_systems=None):
    """Updates a system group"""
    if name is None or org is None:
        raise InvalidInputError('name and org should be provided to '
                                'execute this task')
    cmd = 'system_group update --name {0} --org {1} '.format(name, org)
    if new_name is not None:
        cmd = cmd + '--new_name {0} '.format(new_name)
    if new_description is not None:
        cmd = cmd + '--description {0}'.format(new_description)
    if new_max_systems is not None:
        cmd = cmd + '--max_systems {0}'.format(new_max_systems)
    run_command(cmd)
    if new_name is not None:
        return new_name
