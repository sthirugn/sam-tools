"""
Module for deletion of sam cli objects
"""

from helper import InvalidInputError, run_command


def delete_org(name):
    """Deletes an org."""
    if name is None:
        raise InvalidInputError('name should be provided to execute this task')
    run_command('org delete --name={0}'.format(name))


def delete_activation_key(name, org):
    """Deletes an activation key."""
    if name is None or org is None:
        raise InvalidInputError('name and org should be provided to '
                                'execute this task')
    run_command('activation_key delete --name {0} --org {1}'.format(name, org))


def delete_user(username):
    """Deletes an user"""
    if username is None:
        raise InvalidInputError('username should be provided to execute '
                                'this task')
    run_command('user delete --username {0}'.format(username))


def delete_role(name):
    """Creates an user role"""
    if name is None:
        raise InvalidInputError('name should be provided to execute this task')
    run_command('user_role delete --name {0}'.format(name))


def delete_permission(name, user_role):
    """Creates a permission"""
    if name is None or user_role is None:
        raise InvalidInputError('name and user_role should be provided to '
                                'execute this task')
    cmd = ('permission delete --name {0} '
           '--user_role {1}').format(name, user_role)
    run_command(cmd)


def delete_distributor(name, org):
    """Deletes a distributor"""
    if name is None or org is None:
        raise InvalidInputError('name and org should be provided to '
                                'execute this task')
    run_command('distributor delete --name {0} --org {1}'.format(name, org))


def delete_system(name, org):
    """Deletes a system"""
    if name is None or org is None:
        raise InvalidInputError('name and org should be provided to '
                                'execute this task')
    run_command('system unregister --name {0} --org {1}'.format(name, org))


def delete_system_group(name, org):
    """Deletes a system group"""
    if name is None or org is None:
        raise InvalidInputError('name and org should be provided to '
                                'execute this task')
    run_command('system_group delete --name {0} --org {1}'.format(name, org))
