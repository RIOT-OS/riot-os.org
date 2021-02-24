#!/bin/bash

# Parse RIOT statistics and dump them
#
# Usage:
#  $ ./riot-stats.sh repo
# * repo: path to RIOT's repository

CDIR=`pwd`
RIOTBASE=$1

countboards () {
  cd $RIOTBASE
  make info-boards | tr " " "\n" | wc -l | xargs printf "boards: %d\n" 
  cd - > /dev/null
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

contributors () {
  echo
}

countboards
countcpus
countcommits
