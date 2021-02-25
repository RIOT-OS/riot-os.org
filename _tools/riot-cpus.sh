#!/bin/bash

# Parse RIOT cpus and dump them in YAML format
#
# Usage:
#  $ ./riot-cpus.sh repo
# * repo: path to RIOT's repository

RIOTBASE=$1
URL_PREFIX=https://doc.riot-os.org/group__

# Get CPU list from KConfig files.
# The CPU is listed in the "default" option next to the CPU symbol.
# `awk` and `sed` are used to extract and format these values.

cpulist () {
    git -C $RIOTBASE grep -A1 "config CPU$" cpu/ | grep "Kconfig" | \
        grep default | awk '{print $3}' | sed 's/"//g'
}

parsecpu () {
    for cpu in $(cpulist)
    do
        git -C $RIOTBASE grep "defgroup\s*cpu_$cpu\s" cpu/ | \
            URL_PREFIX=$URL_PREFIX awk '
                {
                    # Set the group name to a[1] and the description to a[2]
                    match($0, "defgroup\\s*(\\w+)\\s+(.*)$", a);

                    # Replace every underscore with double underscore in order
                    # to build Doxygen links
                    gsub(/_/, "__", a[1]);

                    # Generate YAML
                    print "- name: " a[2] "\n  apiurl: " prefix a[1] ".html"
                }' prefix=$URL_PREFIX

    done
}

parsecpu
