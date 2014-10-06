"""
Module for sam cli tests and smoke tests
"""

from fauxfactory import gen_string
from tasks import create, delete, info, manifest, update


def run_smoke_test():
    """Runs basic smoke test"""
    # Create Org
    org = create.create_org()

    # Create Activation Key
    create.create_activation_key(org=org)

    # Create User
    create.create_user()

    # Create Role
    create.create_role()

    # Create Permission
    create.create_permission()

    # Create Distributor
    create.create_distributor(org=org)

    # Create System
    create.create_system(org=org)

    # Create System group
    create.create_system_group(org=org)

    # Import Manifest, Get info, Delete Manifest
    manifest.import_manifest(org=org, deleted=False)
    manifest.refresh_manifest(org=org)
    info.get_product_list(org=org)
    info.get_provider_list(org=org)
    info.get_environment_list(org=org)
    manifest.delete_manifest(org=org)

    # Run some basic commands
    info.run_ping_command()
    info.run_version_command()
    info.run_about_command()


def delete_tests():
    """Runs delete tests"""
    # Create Org and delete at the end of the test
    org = create.create_org()

    # Create/Delete activation key
    activation_key = create.create_activation_key(org=org)
    delete.delete_activation_key(name=activation_key, org=org)

    # Create/Delete user
    username = create.create_user()
    delete.delete_user(username)

    # Create/Delete role and permission
    role_name = create.create_role()
    permission_name = create.create_permission(user_role=role_name)
    delete.delete_permission(name=permission_name, user_role=role_name)
    delete.delete_role(role_name)

    # Create/Delete Distributor
    distributor_name = create.create_distributor(org=org)
    delete.delete_distributor(name=distributor_name, org=org)

    # Create/Delete System
    system_name = create.create_system(org=org)
    delete.delete_system(name=system_name, org=org)

    # Create/Delete System group
    system_group_name = create.create_system_group(org=org)
    delete.delete_system_group(name=system_group_name, org=org)

    # Delete Org
    delete.delete_org(org)


def update_tests():
    """Runs update tests"""
    # Create and update Org
    org = create.create_org()
    update.update_org(name=org, new_description='test')
    info.get_org(name=org)

    # Create and update activation key
    ack_key = create.create_activation_key(org=org)
    new_ack_key = gen_string("alphanumeric", 6)
    update.update_activation_key(name=ack_key, org=org, new_name=new_ack_key,
                                 new_description='testdesc1', new_limit='5')
    info.get_activation_key(name=new_ack_key, org=org)

    # Create and update user
    user = create.create_user()
    new_user = update.update_user(username=user, new_password='password',
                                  new_email='test@test.com',
                                  new_default_organization='ACME_Corporation',
                                  new_default_locale='en')
    info.get_user(new_user)

    # Create and update role
    role = create.create_role()
    new_role = gen_string("alphanumeric", 6)
    update.update_role(name=role, new_name=new_role,
                       new_description='roletest1')
    info.get_role(new_role)

    # Create multiple permissions for a role and list them
    # No update option for permission
    create.create_permission(user_role=new_role)
    create.create_permission(user_role=new_role)
    info.get_permission(user_role=new_role)

    # Create and update distributor
    distributor = create.create_distributor(org=org)
    updated_distributor = gen_string("alphanumeric", 6)
    update.update_distributor(name=distributor, org=org,
                              new_name=updated_distributor,
                              new_description=updated_distributor)
    info.get_distributor(name=updated_distributor, org=org)

    # Create and update system
    system = create.create_system(org=org)
    updated_system = gen_string("alphanumeric", 6)
    # known bug - system update will fail in cli
    update.update_system(name=system, org=org,
                         new_name=updated_system,
                         new_description=updated_system)
    info.get_system(name=updated_system, org=org)

    # Create and update system group
    system_group = create.create_system_group(org=org)
    updated_system_group = gen_string("alphanumeric", 6)
    update.update_system_group(name=system_group, org=org,
                               new_name=updated_system_group,
                               new_description=updated_system_group,
                               new_max_systems=5)
    info.get_system_group(name=updated_system_group, org=org)
