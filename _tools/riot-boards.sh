#!/bin/bash

# Parse RIOT boards and dump them in YAML format
#
# Usage:
#  $ ./riot-boards.sh repo
# * repo: path to RIOT's repository

RIOTBASE=$1
URL_PREFIX=https://doc.riot-os.org/group__

# Extract board names from Doxygen's defgroup. Exclude common and config files.
listboards () {
    grep -R --include doc.txt defgroup $RIOTBASE/boards | grep -v "common" | \
        grep -v "config"
}
parseboards () {
     listboards | \
    awk '
        /boards_/ {
            # Extract group and name of the board
            match($0, "(boards_[a-zA-Z0-9\\-_]+)\\s+(.*)$",a);
            group = a[1];
            name = a[2];

            # Replace underscores with double underscores in order to generate
            # Doxygen links
            gsub("_", "__", group);

            # Generate the YAML file
            print "- name: " name "\n  apiurl: " url group ".html"
        }
        ' url=$URL_PREFIX
}

parseboards
