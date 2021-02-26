#!/bin/bash

# Parse RIOT driver categories and dump them in CSV format
#
# Usage:
#  $ ./riot-drivers-cats.sh repo
# * repo: path to RIOT's repository

RIOTBASE=$1

parsedriverscats () {
    git -C $RIOTBASE grep -h -A1 -B1 defgroup drivers/doc.txt | \
        awk -F " " '
            # Add CSV header
            BEGIN {
                print "group,name"
            } 

            # Extract group and name from the defgroup tag
            /defgroup\s+drivers_/ {
                match($0, "defgroup\\s+(\\w+)\\s*(.*$)", a);
                print a[1] "," a[2]
            }
        '
}

parsedriverscats
