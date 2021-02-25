#!/bin/bash

# Parse RIOT drivers and dump them in CSV format
#
# Usage:
#  $ ./riot-drivers.sh repo
# * repo: path to RIOT's repository

RIOTBASE=$1

parsedrivers () {
    cd $RIOTBASE
    echo "parent,group,name";git grep defgroup drivers/doc.txt | awk -F " " '/defgroup\s+drivers_/ {print $4}' | xargs -I % sh -c 'git grep -h -B 5 -A 5 "ingroup\s*%$" | awk "{print \"%:\" \$0}"' | grep defgroup | awk '{match($0, "(^.*):.*defgroup\\s+(\\w*)\\s*(.*$)",a); print a[1] "," a[2] "," a[3]}'
    cd - > /dev/null
}

parsedrivers
