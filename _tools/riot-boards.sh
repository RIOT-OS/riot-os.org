#!/bin/bash

# Parse RIOT boards and dump them in YAML format
#
# Usage:
#  $ ./riot-boards.sh repo
# * repo: path to RIOT's repository

RIOTBASE=$1

parseboards () {
    cd $RIOTBASE
    grep -R --include doc.txt defgroup ./boards | grep -v "common" | grep -v "config" | \
    awk '/boards_/ {match($0, "(boards_[a-zA-Z0-9\\-_]+)\\s+(.*)$",a); file = a[1] ; board = a[2]; url = "https://doc.riot-os.org/group__"; gsub("_", "__", file); print "- name: " board "\n  apiurl: " url file ".html"}'
    cd - > /dev/null
}

parseboards
