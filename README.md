sam-tools
================

To run automation tests:

1. git clone this repo
2. Copy env_sample.sh and name it env.sh. Update required parameters as necessary
3. To run a specific task

```
fab -H $hostname -u $user create_org
```
4. To see all the available tasks
```
fab --list
```

Note:
It is better to place your ssh public key in the host or add -p <password> to your fab command
