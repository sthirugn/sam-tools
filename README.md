sam-tools
================
To run a specific task

```
fab -H $hostname -u $user create_org
```

Test Assumptions:
* MANIFEST_URL = "/tmp/test_sam_manifest.zip" - This assumes that this manifest file is in tmp folder of the host. Otherwise manifest test will fail.

Note:
It is better to place your ssh public key in the host so you can avoid typing password.
