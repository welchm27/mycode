#!/usr/bin/env python3

import shutil
import os


def main():
    # start in the home directory
    os.chdir('/home/student/mycode/')

    # move a file or folder from source to dest
    shutil.move('raynor.obj', 'ceph_storage/')

    # prompt user for new name of file
    xname= input('What is the new name for kerrigan.obj? ')
    # move and rename the file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)





if __name__ == "__main__":
    main()
