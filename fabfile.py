"""
Python Module for sam tests
"""

from fabric.api import env
from helper import get_host, get_test_username
from tasks import create, delete, info, install, manifest, tests, update

# Append host from config file
env.hosts = get_host(env.hosts)

# Override user from config file, if specified
env.user = get_test_username(env.user)


# Test APIs
def run_smoke_test():
    """Runs basic smoke test"""
    tests.run_smoke_test()


def delete_tests():
    """Runs delete tests"""
    tests.delete_tests()


def update_tests():
    """Runs update tests"""
    tests.update_tests()


def run_all_tests():
    """Runs all tests"""
    tests.run_smoke_test()
    tests.delete_tests()
    tests.update_tests()


# Install APIs
def clean_headpin():
    """Resets and cleans headpin

    WARNING: All data will be lost
    """
    install.clean_headpin()


def cdn_install():
    """Installs sam from cdn"""
    install.cdn_install()


def install_from_repo():
    """Task to install SAM from repo URL

    Note:
    Following environment variables are must to continue:
    - RH_PORTAL_USERNAME
    - RH_PORTAL_PASSWORD
    - BASE_URL

    """
    install.install_from_repo()


def register_subscribe():
    """Registers and subscribes to portal

    Note:
    Following environment variables are must to continue:
    - RH_PORTAL_USERNAME
    - RH_PORTAL_PASSWORD

    """
    install.register_subscribe()


def clean_rhsm():
    """Removes pre-existing Candlepin certs and resets RHSM."""
    install.clean_rhsm()

def client_registration_test():
    """Register client against sam and runs tests
    
    Note:
    Following environment variables are must to continue:
    - ORG
    - ACTIVATIONKEY
    - CERTURL
    """
    install.client_registration_test()

# Create APIs
def create_org(name=None):
    """Creates an org."""
    return create.create_org(name)


def create_activation_key(name=None, org=None, description=None,
                          limit=None):
    """Creates an activation key."""
    return create.create_activation_key(name, org, description, limit)


def create_user(username=None, password=None, email=None,
                default_organization=None, default_locale=None):
    """Creates an user"""
    return create.create_user(username, password, email,
                              default_organization, default_locale)


def create_role(name=None, description=None):
    """Creates an user role"""
    return create.create_role(name, description)


def create_permission(name=None, user_role=None, description=None, scope=None,
                      verbs=None):
    """Creates a permission"""
    return create.create_permission(name, user_role, description, scope,
                                    verbs)


def create_distributor(name=None, org=None):
    """Creates a distributor"""
    return create.create_distributor(name, org)


def create_system(name=None, org=None):
    """Creates a system"""
    return create.create_system(name, org)


def create_system_group(name=None, org=None):
    """Creates a system group"""
    return create.create_system_group(name, org)


# Manifest APIs
def import_manifest(org=None, filepath=None, deleted=True):
    """Imports a manifest

    If delete is set to False, the manifest will not be deleted and the user
    has to handle the deletion manually or by calling delete_manifest

    """
    manifest.import_manifest(org, filepath, deleted)


def refresh_manifest(org=None):
    """Refreshes a manifest"""
    manifest.refresh_manifest(org)


def delete_manifest(org=None):
    """Deletes a manifest"""
    manifest.delete_manifest(org)


# Delete APIs
def delete_org(name):
    """Deletes an org."""
    delete.delete_org(name)


def delete_activation_key(name, org):
    """Deletes an activation key."""
    delete.delete_activation_key(name=name, org=org)


def delete_user(username):
    """Deletes an user"""
    delete.delete_user(username)


def delete_role(name):
    """Creates an user role"""
    delete.delete_role(name)


def delete_permission(name, user_role):
    """Creates a permission"""
    delete.delete_permission(name, user_role)


def delete_distributor(name, org):
    """Deletes a distributor"""
    delete.delete_distributor(name, org)


def delete_system(name, org):
    """Deletes a system"""
    delete.delete_system(name, org)


def delete_system_group(name, org):
    """Deletes a system group"""
    delete.delete_system_group(name, org)


# Update APIs
def update_org(name, new_description=None):
    """Updates an org."""
    return update.update_org(name, new_description)


def update_activation_key(name, org, new_name=None, new_description=None,
                          new_limit=None):
    """Updates an activation key."""
    return update.update_activation_key(name, org, new_name,
                                        new_description, new_limit)


def update_user(username, new_password=None, new_email=None,
                new_default_organization=None, new_default_locale=None):
    """Updates an user"""
    return update.update_user(username, new_password, new_email,
                              new_default_organization, new_default_locale)


def update_role(name, new_name=None, new_description=None):
    """Updates a role"""
    return update.update_role(name, new_name, new_description)


def update_distributor(name, org, new_name=None, new_description=None):
    """Updates a distributor"""
    return update.update_distributor(name, org, new_name, new_description)


def update_system(name, org, new_name=None, new_description=None):
    """Updates a system"""
    return update.update_system(name, org, new_name, new_description)


def update_system_group(name, org, new_name=None, new_description=None,
                        new_max_systems=None):
    """Updates a system group"""
    return update.update_system_group(name, org, new_name, new_description,
                                      new_max_systems)


# Get APIs
def get_product_list(org=None):
    """Get list of Products for an org"""
    info.get_product_list(org)


def get_provider_list(org=None):
    """Get list of Providers for an org"""
    info.get_provider_list(org)


def get_environment_list(org=None):
    """Get list of Environments for an org"""
    info.get_environment_list(org)


def run_ping_command():
    """Runs ping command"""
    info.run_ping_command()


def run_version_command():
    """Runs version command"""
    info.run_version_command()


def run_about_command():
    """Runs about command"""
    info.run_about_command()


def get_org(name):
    """Gets an org"""
    info.get_org(name)


def get_activation_key(name, org):
    """Gets an activation key"""
    info.get_activation_key(name, org)


def get_user(username):
    """Gets an user"""
    info.get_user(username)


def get_role(name):
    """Gets a role"""
    info.get_role(name)


def get_permission(user_role):
    """Gets permissions for a role"""
    info.get_permission(user_role)


def get_distributor(name, org):
    """Gets a distributor"""
    info.get_distributor(name, org)


def get_system(name, org):
    """Gets a system"""
    info.get_system(name, org)


def get_system_group(name, org):
    """Gets a system group"""
    info.get_system_group(name, org)
