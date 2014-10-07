"""
Module for installation of sam
"""

import os
import sys

from fabric.api import put, run
from helper import get_config
from tasks.info import run_ping_command
from StringIO import StringIO


def clean_headpin():
    """Resets and cleans headpin

    WARNING: All data will be lost

    """
    print ('Attempting to clean headpin...This may take a few minutes. '
           'You will be notified in case of errors')
    run('katello-configure --deployment=sam --reset-data=YES'
        '--reset-cache=YES', quiet=True)


def register_subscribe():
    """Registers and subscribes to portal

    Note:
    Following samtools.properties config values are must to continue:
    - rh_portal_username
    - rh_portal_password

    """
    rh_portal_username = get_config('samtools', 'rh_portal_username')
    rh_portal_password = get_config('samtools', 'rh_portal_password')

    if rh_portal_username is None or rh_portal_password is None:
        print ('Missing Parameters: rh_portal_username AND rh_portal_password '
               'must be defined in samtools.properties to continue '
               'installation')
        sys.exit(1)

    # Subscribe to RH portal
    run('subscription-manager register --username="{0}" --password="{1}" '
        '--autosubscribe --force'.format(rh_portal_username,
                                         rh_portal_password))


def cdn_install():
    """Installs sam from cdn

    Note:
    Following samtools.properties config values are must to continue:
    - rh_portal_username
    - rh_portal_password
    """
    # Register and subscribe the host to portal
    register_subscribe()

    # Disable unwanted repos
    run('yum-config-manager --disable "*"', quiet=True)

    # Enable rhel6 repos and sam repos
    run('yum-config-manager --enable rhel-6-server-rpms')
    run('yum-config-manager --enable rhel-6-server-sam-rpms')

    # Install sam
    run('yum install -y katello-headpin-all')

    # Run katello-configure
    run('katello-configure --deployment=sam --user-pass=admin')


def install_from_repo():
    """Task to install SAM from repo URL

    Note:
    Following samtools.properties config values are must to continue:
    - rh_portal_username
    - rh_portal_password
    - base_url

    """
    base_url = get_config('samtools', 'base_url')

    if base_url is None:
        print ('Missing Parameters: base_url must be defined in '
               'samtools.properties to continue installation')
        sys.exit(1)

    # Register and subscribe
    register_subscribe()

    # Disable unwanted repos
    print 'Disabling all repos...'
    run('yum-config-manager --disable "*"', quiet=True)

    # Enable rhel6 repos only
    run('yum-config-manager --enable rhel-6-server-rpms')

    sam_repo = StringIO()
    sam_repo.write('[sam]\n')
    sam_repo.write('name=sam\n')
    sam_repo.write('baseurl={0}\n'.format(base_url))
    sam_repo.write('enabled=1\n')
    sam_repo.write('gpgcheck=0\n')
    put(local_path=sam_repo,
        remote_path='/etc/yum.repos.d/sam.repo')
    sam_repo.close()

    # Install sam
    run('yum install -y katello-headpin-all')

    # Run katello-configure
    run('katello-configure --deployment=sam --user-pass=admin')

    # Run ping test
    run_ping_command()


def client_registration_test():
    """Register client against sam and runs tests.

    Note:
    Following environment variables are must to continue:
    - ORG
    - ACTIVATIONKEY
    - CERTURL
    """

    # Since all arguments are turned to string, if no defaults are
    # used...

    # Org
    org = os.getenv('ORG', 'Default_Organization')

    # Activation Key
    act_key = os.getenv('ACTIVATIONKEY')

    if not act_key:
        print "You need to provide an activationkey."
        sys.exit(1)

    # Candlepin cert RPM
    cert_url = os.getenv('CERTURL')
    if not cert_url:
        print "You need to install the Candlepin Cert RPM."
        sys.exit(1)

    # If this is a Beaker box, 'disable' Beaker repos
    run('mv /etc/yum.repos.d/beaker* .', warn_only=True)

    # Install the cert file
    run('rpm -Uvh {0}'.format(cert_url), warn_only=True)

    # Register and subscribe
    print "Register/Subscribe using Subscription-manager."
    run('subscription-manager register --force'
        ' --org="{0}"'
        ' --activationkey="{1}"'
        ''.format(org, act_key))
    print "Refreshing Subscription-manager."
    run('subscription-manager refresh')
    print "Performing yum clean up."
    run('yum clean all', quiet=True)
    print "'Firefox' and 'Telnet' should not be installed."
    run('rpm -q firefox telnet', warn_only=True)
    print "Installing 'Firefox' and 'Telnet'."
    run('yum install -y firefox telnet', quiet=True)
    print "'Firefox' and 'Telnet' should be installed."
    run('rpm -q firefox telnet')
    print "Removing 'Firefox' and 'Telnet'."
    run('yum remove -y firefox telnet', quiet=True)
    print "Checking if 'Firefox' and 'Telnet' are installed."
    run('rpm -q firefox telnet', warn_only=True)
    print "Installing 'Web Server' group."
    run('yum groupinstall -y "Web Server"', quiet=True)
    print "Checking for 'httpd' and starting it."
    run('rpm -q httpd')
    run('service httpd start', warn_only=True)
    print "Stopping 'httpd' service and remove 'Web Server' group."
    run('service httpd stop', warn_only=True)
    run('yum groupremove -y "Web Server"', quiet=True)
    print "Checking if 'httpd' is really removed."
    run('rpm -q httpd', warn_only=True)

    # Clean up
    # Unregisters a machine from Red Hat
    run('subscription-manager unregister', warn_only=True)
    run('subscription-manager clean')

    # clean up rhsm
    clean_rhsm()


def clean_rhsm():
    # pylint: disable=W1401
    """Removes pre-existing Candlepin certs and resets RHSM."""
    print "Erasing existing Candlepin certs, if any."
    run('yum erase -y $(rpm -qa |grep candlepin-cert-consumer)',
        warn_only=True, quiet=True)
    print "Resetting rhsm.conf to point to cdn."
    run("sed -i -e 's/^hostname.*/hostname=subscription.rhn.redhat.com/' "
        "/etc/rhsm/rhsm.conf")
    run("sed -i -e 's/^prefix.*/prefix=\/subscription/' /etc/rhsm/rhsm.conf")
    run("sed -i -e 's/^baseurl.*/baseurl=https:\/\/cdn.redhat.com/' "
        "/etc/rhsm/rhsm.conf")
    run("sed -i -e 's/^repo_ca_cert.*/repo_ca_cert=%(ca_cert_dir)"
        "sredhat-uep.pem/' /etc/rhsm/rhsm.conf")
