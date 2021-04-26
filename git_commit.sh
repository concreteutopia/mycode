#!/bin/bash

comment=$1

cd ~/mycode
git add *
git commit -m "$1"
git push origin main
