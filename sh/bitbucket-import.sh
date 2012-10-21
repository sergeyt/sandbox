#!/bin/bash
# Import a (svn) workspace into my bitbucket account

WS=${1?}
set -o errexit
cd $WS
find . -name .svn -type d | xargs rm -rf
git init
git remote add origin ssh://git@bitbucket.org/ymattw/$WS
git add .
git ci -m 'initial import'
git push
git push -u origin master

# EOF
