#!/usr/bin/env python3

import shutil
import os

#change directories
os.chdir('/home/student/mycode/')

#move raynor.obj to ceph_storage
shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj? ')

#rename kerrigan.obj to filename provided by user
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


