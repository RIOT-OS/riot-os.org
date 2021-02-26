#!/bin/bash

# Parse RIOT drivers and dump them in CSV format
#
# Usage:
#  $ ./riot-drivers.sh repo
# * repo: path to RIOT's repository

RIOTBASE=$1

# Get the driver groups from Doxygen's defgroup tag
listdrivergroups () {
    git -C $RIOTBASE grep defgroup drivers/doc.txt | \
        awk -F " " '/defgroup\s+drivers_/ {print $4}' 
}

listbytype () {
    git -C $RIOTBASE grep -h -B 5 -A 5 "ingroup\s*$1\$" | grep defgroup
}

parsedrivers () {
    echo "parent,group,name"

    for group in $(listdrivergroups)
    do
        listbytype "$group" | \
            awk '
                    {
                        # Extract driver group and name
                        match($0, "defgroup\\s+(\\w*)\\s*(.*$)",a);
                        
                        # Create CSV (parent, group, name)
                        print parent "," a[1] "," a[2]
                    }
                ' parent=$group
    done
}

parsedrivers
