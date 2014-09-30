"""
Python Module for sam tests
"""

from fabric.api import run
from fauxfactory import gen_string, gen_integer, gen_email

USER_NAME = 'admin'
USER_PASSWORD = 'admin'
MANIFEST_URL = "/tmp/test_sam_manifest.zip"
PROVIDER_NAME = "Red Hat"


class InvalidInputError(Exception):
    """Indicates an invalid input error"""


def _run_command(cmd=None):
    """Executes the actual command"""
    basic_cmd = 'headpin -u {0} -p {1} '.format(USER_NAME, USER_PASSWORD)
    if cmd is not None:
        basic_cmd = basic_cmd + cmd
    run('%s' % basic_cmd)


def run_basic_commands():
    """Runs basic sam server commands"""
    _run_command('ping')
    _run_command('version')
    _run_command('about')


def create_org(name=None):
    """Creates an org."""
    if name is None:
        name = gen_string("alphanumeric", 10)
    _run_command('org create --name={0}'.format(name))
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
    _run_command('activation_key create --name {0} --org {1} --description {2}'
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
        cmd = cmd + '--default_organization {0}'.format(default_organization)
    if default_locale is not None:
        cmd = cmd + '--default_locale {0}'.format(default_locale)
    _run_command(cmd)
    return username


def create_role(name=None, description=None):
    """Creates an user role"""
    if name is None:
        name = gen_string("alphanumeric", 10)
    if description is None:
        description = gen_string("alphanumeric", 10)
    _run_command('user_role create --name {0} --description {1}'.format(
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
    cmd = ('permission create --name {0} --user_role {1} ' +
           '--description {2} --scope {3} --verbs {4}')
    cmd = cmd.format(name, user_role, description, scope, verbs)
    _run_command(cmd)
    return name


def create_distributor(name=None, org=None):
    """Creates a distributor"""
    if name is None:
        name = gen_string("alphanumeric", 10)
    if org is None:
        org = create_org()
    _run_command('distributor create --name {0} --org {1}'.format(name, org))
    return name


def create_system(name=None, org=None):
    """Creates a system"""
    if name is None:
        name = gen_string("alphanumeric", 10)
    if org is None:
        org = create_org()
    _run_command('system register --name {0} --org {1}'.format(name, org))
    return name


def create_system_group(name=None, org=None):
    """Creates a system group"""
    if name is None:
        name = gen_string("alphanumeric", 10)
    if org is None:
        org = create_org()
    _run_command('system_group create --name {0} --org {1}'.format(name, org))
    return name


def import_manifest(org=None, filepath=None, delete=True):
    """Imports a manifest

    If delete is set to False, the manifest will not be deleted and the user
    has to handle the deletion manually or by calling delete_manifest

    """
    if org is None:
        org = create_org()
    if filepath is None:
        filepath = MANIFEST_URL
    cmd = 'provider import_manifest create --name "{0}" --org {1} --file "{2}"'
    cmd = cmd.format(PROVIDER_NAME, org, filepath)
    _run_command(cmd)
    if delete is True:
        print ('*** After manifest import it will be deleted so as',
               ' to reuse it ***')
        delete_manifest(org)


def refresh_manifest(org=None):
    """Refreshes a manifest"""
    if org is None:
        raise InvalidInputError
    cmd = 'provider refresh_manifest --name "{0}" --org {1}'
    cmd = cmd.format(PROVIDER_NAME, org)
    _run_command(cmd)


def delete_manifest(org=None):
    """Deletes a manifest"""
    if org is None:
        raise InvalidInputError
    cmd = 'provider delete_manifest --name "{0}" --org {1}'
    cmd = cmd.format(PROVIDER_NAME, org)
    _run_command(cmd)


def run_smoke_test():
    """Runs basic smoke test"""
    run_basic_commands()
    org = create_org()
    activation_key = create_activation_key(org=org)
    user = create_user()
    role = create_role()
    permission = create_permission()
    distributor = create_distributor(org=org)
    system = create_system(org=org)
    system_group = create_system_group(org=org)
    import_manifest(org=org, delete=False)
    refresh_manifest(org=org)
    delete_manifest(org=org)
    output = ('org={0} ak={1} user={2} role={3} permission={4} ' +
              'distributor={5} system={6} system_group={7}')
    output = output.format(org, activation_key, user, role, permission,
                           distributor, system, system_group)
    print output
