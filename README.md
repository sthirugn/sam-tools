sam-tools
================

To run automation tests:

1. git clone this repo
2. Copy env_sample.sh and name it env.sh. Update required parameters as necessary
3. To see all the available tasks
```
# fab --list
```
4. It is very easy to run a specific task

```
# fab -H $hostname -u $user create_org
```

Note:
It is better to place your ssh public key in the host or add ```-p <password>``` to your fab command

Code Contribution:
1. git clone this repo
2. Make necessary code changes
3. Run local tests and validate the code
4. Make sure pylint and flake8 pass
```
# make lint
# make flake8
```
