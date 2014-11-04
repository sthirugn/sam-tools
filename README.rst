sam-tools
=========

Python pre-requisites:

1. Install Python header files. The package providing these files varies per
distribution. For example:

* Fedora 20 provides header files in the `python-devel`_ package::
   
   yum install python-devel

2. Install pip::

    wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py
    python get-pip.py

    (or)

    sudo yum install python-pip

To run automated tests:

1. Get the source code and install dependencies::

    git clone git@github.com:sthirugn/sam-tools.git
    cd sam-tools
    pip install -r requirements.txt

2. Copy `samtools.properties.sample` and name it `samtools.properties` (referred
   to as the 'config file' in this doc). Update required parameters in the
   config file.
3. To see all the available tasks::

    fab --list

4. To run a specific task::

    fab -H <hostname> -u <user> create_org

5. You can specify the 'host' and 'user' options in the config file if you want
   to work with just one host as a single user. This done, the command becomes
   much simpler::

    fab create_org

Note: the 'user' config file option defaults to your current user.

Note: It is better to place your ssh public key in the host or add `-p
<password>` to your fab command.

Code Contribution
-----------------

1. git clone this repo
2. Make necessary code changes
3. Run local tests and validate the code
4. Make sure pylint and flake8 pass::

    make lint
    make flake8


Known Issues
------------

If you are using rhel, you may find problems invoking fab command. Please
check `stackoverflow`_ recommended solution (look for the solution which tells
to comment out number.py) to fix this.

.. _python-devel: https://apps.fedoraproject.org/packages/python-devel
.. _python-dev: http://packages.ubuntu.com/trusty/python-dev
.. _stackoverflow: http://stackoverflow.com/questions/24373162/fabric-on-oracle-linux-6-5-fails-with-pkg-resources-distributionnotfound-param

