#!/usr/bin/env bash
# Runs on shippable. tags branchs as it stands and pushes tags to github.

# stop processing on any statement return != 0
set -e

# Use deploy switch on setup.py to install deploy deps.
pip install -q -e .[deploy]

# version.py will return "pypyr x.y.z python a.b.c" - get everything after the
# space for the bare version number.
NEW_VERSION=`python pypyrslack/version.py | cut -d " " -f2`
echo "New version is: ${NEW_VERSION}"
TAG_NAME="v${NEW_VERSION}"

# all done, clean-up
pip uninstall -y pypyr

if [ $(git tag -l "${TAG_NAME}") ]; then
    echo "----------tag already exists.----------------------------------------"
else
    echo "version tag doesn't exist. create tag. ${TAG_NAME}"
    git tag "${TAG_NAME}"
    # use the key that Shippable uses to connect to GitHub
    git remote set-url origin git@github.com:${ORG_NAME}/${REPO_NAME}.git
    ssh-agent bash -c 'ssh-add /tmp/ssh/sshpypyr; git push origin --tags'
fi;
