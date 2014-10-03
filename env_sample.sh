#!/bin/bash

export RH_PORTAL_USERNAME='secret@secret.com'
echo 'RH_PORTAL_USERNAME is set'

export RH_PORTAL_PASSWORD='ToPsEcRet'
echo 'RH_PORTAL_PASSWORD is set'

export BASE_URL='Path to install source'
echo 'BASE_URL is set'

# Do the following steps before running automation:
# 1. Copy this shell script and rename to 'env.sh'
# 2. Update necessary parameters for the automation run
# 3. Run this shell script in your terminal using: # source env.sh