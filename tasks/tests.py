"""
Python Module for sam tests
"""

from tasks import create, delete, info, manifest


def run_smoke_test():
    """Runs basic smoke test"""
    org = create.create_org()
    create.create_activation_key(org=org)
    create.create_user()
    create.create_role()
    create.create_permission()
    create.create_distributor(org=org)
    create.create_system(org=org)
    create.create_system_group(org=org)
    manifest.import_manifest(org=org, delete=False)
    manifest.refresh_manifest(org=org)
    info.get_product_list(org=org)
    info.get_provider_list(org=org)
    info.get_environment_list(org=org)
    manifest.delete_manifest(org=org)
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
