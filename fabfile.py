"""
Python Module for sam tests
"""

from tasks import create, delete, info, install, manifest, tests


# Test APIs
def run_smoke_test():
    """Runs basic smoke test"""
    tests.run_smoke_test()


def delete_tests():
    """Runs delete tests"""
    tests.delete_tests()


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
    return create_system_group(name, org)


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
