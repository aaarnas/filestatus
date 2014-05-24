import os
import sys

def countFileData(filepath, words_dict, letters_dict):
    with open(filepath, 'r') as file:
        for line in file:
            for word in line.split():
                word = word.lower()
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1
                for letter in word:
                    if letter in letters_dict:
                        letters_dict[letter] += 1
                    else:
                        letters_dict[letter] = 1


def printPathStatus(path):
    print "Path '%s' information:" % (path)
    file_path = ""
    total_words_dict = {}
    total_letters_dict = {}
    for file in os.listdir(path):
        file_path = path
        if not path.endswith('/'):
            file_path += "/"
        file_path += file
        if os.path.isfile(file_path):
            words_dict = {}
            letters_dict = {}
            countFileData(file_path, words_dict, letters_dict)
            total_words_dict = {k: total_words_dict.get(k, 0) +
                    words_dict.get(k, 0) for k in set(total_words_dict)
                    | set(words_dict)}
            total_letters_dict = {k: total_letters_dict.get(k, 0) +
                    letters_dict.get(k, 0) for k in set(total_letters_dict)
                    | set(words_dict)}

    print "Most common words in '%s'" % (path)
    words_list = sorted(words_dict.items(), key=lambda x:x[1], reverse=True)
    i = 0
    for item in words_list:
        i += 1
        if i > 10:
            break
        print "%s - %d" % (item[0], item[1])

    print "Most common letters in '%s'" % (path)
    letters_list = sorted(letters_dict.items(),
            key=lambda x:x[1], reverse=True)
    i = 0
    for item in letters_list:
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


