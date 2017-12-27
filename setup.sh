#!/bin/bash

deactivate
rm -rf sandbox

pip install virtualenv
virtualenv sandbox
cd sandbox
. bin/activate
pip install hdfs