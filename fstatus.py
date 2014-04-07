import os
import sys

def countWords(filepath, words_dict):
    with open(filepath, 'r') as file:
        for line in file:
            for word in line.split():
                word = word.lower()
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1


def printPathStatus(path):
    print "Path '%s' information:" % (path)
    file_path = ""
    words_dict = {}
    for file in os.listdir(path):
        file_path = path
        if not path.endswith('/'):
            file_path += "/"
        file_path += file
        if os.path.isfile(file_path):
            countWords(file_path, words_dict)

    print "Most common words in '%s'" % (path)
    words_list = sorted(words_dict.items(), key=lambda x:x[1], reverse=True)
    i = 0
    for item in words_list:
        i += 1
        if i > 10:
            break
        print "%s - %d" % (item[0], item[1])


if len(sys.argv) > 1:
    if os.path.isdir(sys.argv[1]):
        printPathStatus(sys.argv[1])
    else:
        print "Not a path"
else:
    print "No path specified"


