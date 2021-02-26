#!/bin/bash

# Parse RIOT statistics and dump them
#
# Usage:
#  $ ./riot-stats.sh repo
# * repo: path to RIOT's repository

RIOTBASE=$1

countboards () {
  make -C $RIOTBASE info-boards | tr " " "\n" | wc -l | \
      xargs printf "boards: %d\n" 
}

countcpus () {
    git -C $RIOTBASE grep "config CPU_FAM_" | grep "Kconfig" | wc -l | \
        xargs printf "cpus: %d\n"
}

countcommits () {
    git -C $RIOTBASE rev-list --count master | xargs printf "commits: %d\n" 
}

countboards
countcpus
countcommits
