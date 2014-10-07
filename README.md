=========
sam-tools
=========

To run automation tests
-----------------------

1. git clone this repo
2. Copy samtools.properties.sample and name it samtools.properties (referred as 'config file' in this doc)
3. Update required parameters in config file
4. To see all the available tasks

```
	# fab --list
```

4. It is very easy to run a specific task

```
	# fab -H $hostname -u $user create_org
```
5. If you want to run on just one host, you can specify it as 'host' in config file, the command becomes much easier:

```
	# fab create_org
```
Note that Step 5 also requires 'user' value in config file if you want to run it as different user than your current logged on terminal user.

Note:
It is better to place your ssh public key in the host or add ```-p <password>``` to your fab command

Code Contribution
-----------------
1. git clone this repo
2. Make necessary code changes
3. Run local tests and validate the code
4. Make sure pylint and flake8 pass

```
	# make lint
	# make flake8
```
