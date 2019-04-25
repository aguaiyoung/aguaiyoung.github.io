#!/usr/bin/env bash
#
# This script can be used to sync the wiki submodule
# in case you're using github internal wiki option
#

rm -rf Gemfile.lock
rm -rf _site/
git status ./
git add ./
git commit -a -m "updated wiki"
git push origin master
