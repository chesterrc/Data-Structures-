# Name: Chester Corpuz
# OSU Email: corpuzc@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 0
# Due Date: Apr 3 2023
# Description: Checks to see if the python version of the user is compatible 

import sys

cur_version = sys.version_info

if cur_version >= (3,7):
    print("This is an acceptable version of Python, version " + str(cur_version[0]) + '.' + str(cur_version[1]) + '.')
else:
    print("Your Python version is too low, it needs to be 3.7 or greater and this is " + str(cur_version[0]) + '.' + str(cur_version[1]) + '.')


