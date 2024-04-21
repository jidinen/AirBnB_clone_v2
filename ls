#!/usr/bin/bash

if [ "$(which ls | grep -c ls)" == '1' ]; then
   echo "Command Availble"
else
   echo "Command not available"
fi
