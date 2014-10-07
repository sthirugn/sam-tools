sam-tools
=========

To run automated tests:

1. `git clone` this repository.
2. Copy `samtools.properties.sample` and name it `samtools.properties` (referred
   to as the 'config file' in this doc). Update required parameters in the
   config file.
3. To see all the available tasks:

   ```sh
   fab --list
   ```

4. To run a specific task:

   ```sh
   fab -H <hostname> -u <user> create_org
   ```

5. You can specify the 'host' and 'user' options in the config file if you want
   to work with just one host as a single user. This done, the command becomes
   much simpler:

   ```sh
   fab create_org
   ```

Note: the 'user' config file option defaults to your current user.

Note: It is better to place your ssh public key in the host or add `-p
<password>` to your fab command.

Code Contribution
-----------------

1. git clone this repo
2. Make necessary code changes
3. Run local tests and validate the code
4. Make sure pylint and flake8 pass

```sh
make lint
make flake8
```
