import os
import sys

if len(sys.argv) > 1:
    if os.path.isdir(sys.argv[1]):
        print "yes"
    else:
        print "no"
else:
    print "No path specified"
