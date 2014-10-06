"""
Module for creation of sam cli objects
"""

from fauxfactory import gen_email, gen_integer, gen_string
from helper import run_command


def create_org(name=None):
    """Creates an org."""
    if name is None:
        name = gen_string("alphanumeric", 10)
    run_command('org create --name={0}'.format(name))
    return name


def create_activation_key(name=None, org=None, description=None,
                          limit=None):
    """Creates an activation key."""
    if name is None:
        name = gen_string("alphanumeric", 10)
    if org is None:
        org = create_org()
    if description is None:
        description = gen_string("alphanumeric", 10)
    if limit is None:
        limit = gen_integer(min_value=1, max_value=3)
    run_command('activation_key create --name {0} --org {1} --description {2}'
                ' --limit {3}'.format(name, org, description, limit))
    return name


def create_user(username=None, password=None, email=None,
                default_organization=None, default_locale=None):
    """Creates an user"""
    if username is None:
        username = gen_string("alphanumeric", 10)
    if password is None:
        password = gen_string("alphanumeric", 10)
    if email is None:
        email = gen_email("alphanumeric", 10)
    cmd = 'user create --username {0} --password {1} --email {2}'.format(
        username, password, email)
    if default_organization is not None:
        cmd = cmd + ' --default_organization {0}'.format(default_organization)
    if default_locale is not None:
        cmd = cmd + ' --default_locale {0}'.format(default_locale)
    run_command(cmd)
    return username


def create_role(name=None, description=None):
    """Creates an user role"""
    if name is None:
        name = gen_string("alphanumeric", 10)
    if description is None:
        description = gen_string("alphanumeric", 10)
    run_command('user_role create --name {0} --description {1}'.format(
        name, description))
    return name


def create_permission(name=None, user_role=None, description=None, scope=None,
                      verbs=None):
    """Creates a permission"""
    if name is None:
        name = gen_string("alphanumeric", 10)
    if user_role is None:
        user_role = create_role()
    if description is None:
        description = gen_string("alphanumeric", 10)
    if scope is None:
        scope = 'activation_keys'
    if verbs is None:
        verbs = 'read_all'
    cmd = ('permission create --name {0} --user_role {1} '
           '--description {2} --scope {3} '
           '--verbs {4}').format(name, user_role, description, scope, verbs)
    run_command(cmd)
    return name


def create_distributor(name=None, org=None):
    """Creates a distributor"""
    if name is None:
        name = gen_string("alphanumeric", 10)
    if org is None:
        org = create_org()
    run_command('distributor create --name {0} --org {1}'.format(name, org))
    return name


def create_system(name=None, org=None):
    """Creates a system"""
    if name is None:
        name = gen_string("alphanumeric", 10)
    if org is None:
        org = create_org()
    run_command('system register --name {0} --org {1}'.format(name, org))
    return name


def create_system_group(name=None, org=None):
    """Creates a system group"""
    if name is None:
        name = gen_string("alphanumeric", 10)
    if org is None:
        org = create_org()
    run_command('system_group create --name {0} --org {1}'.format(name, org))
    return name
