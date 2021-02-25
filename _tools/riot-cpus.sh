#!/bin/bash

# Parse RIOT cpus and dump them in YAML format
#
# Usage:
#  $ ./riot-cpus.sh repo
# * repo: path to RIOT's repository

RIOTBASE=$1

parsecpu () {
    cd $RIOTBASE
    git grep -A1 "config CPU$" cpu/ | grep "Kconfig" | grep default | awk '{print $3}' | sed 's/"//g' | xargs -I % sh -c 'git grep "defgroup\s*cpu_%\s" cpu/ | awk "{match(\$0, \"defgroup\\\s*(\\\w+)\\\s+(.*)$\", a);gsub(/_/, \"__\", a[1]);print \"- name: \" a[2] \"\n  apiurl: https://doc.riot-os.org/group__\" a[1] \".html\"}"'
    cd - > /dev/null
}

parsecpu
