#!/bin/bash
#
# This script accepts two inputs
# 1. application_name
# 2. application_version

changed="false"
display="This is a simple bash module"
OS="$(uname)"
HOSTNAME="$(uname -n)"

source $1
display="Application Name: $application_name (version: $application_version)"
if [ "$application_name" == "bash" ]; then
  changed="true"
  display="$display - This is a bash App"
fi

printf '{"changed": %s, "msg": "%s", "operating_system": "%s", "hostname": "%s"}' "$changed" "$display" "$OS" "$HOSTNAME" 
exit 0