#!/bin/bash

# Parse RIOT statistics and dump them
#
# Usage:
#  $ ./riot-stats.sh repo
# * repo: path to RIOT's repository

RIOTBASE=$1

countboards () {
  make -C ${RIOTBASE} info-boards | tr " " "\n" | wc -l | xargs printf "boards: %d\n" 
}

countcpus () {
  cd $RIOTBASE
  git grep "config CPU_FAM_" | grep "Kconfig" | wc -l | xargs printf "cpus: %d\n"
  cd - > /dev/null
}

countcommits () {
  cd $RIOTBASE
  git rev-list --count master | xargs printf "commits: %d\n" 
  cd - > /dev/null
}

countboards
countcpus
countcommits
