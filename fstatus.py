import os
import sys

def printPathStatus(path):
    print "Path '%s' information:" % (path)
    dir_list = os.listdir(path)
    for file in dir_list:
        print file

if len(sys.argv) > 1:
    if os.path.isdir(sys.argv[1]):
        printPathStatus(sys.argv[1])
    else:
        print "Not a path"
else:
    print "No path specified"


