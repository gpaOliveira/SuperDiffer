#!/usr/bin/env bash

# install python
apt-get update --yes
apt-get install python-setuptools python-dev python-pip build-essential --yes

# install virtualenv (use --always-copy due to protocol error)
pip install virtualenv
virtualenv venv --always-copy
source venv/bin/activate

# pip install things
venv/bin/pip install -r requirements.txt
venv/bin/python setup.py install
