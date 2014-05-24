import os
import sys

OUTPUT_FILE_PATH = os.getcwd()+'/fList.txt'

def countFileData(filepath, words_dict, symbols_dict):
    try:
        file = open(filepath, 'r')
        for line in file:
            for word in line.split():
                word = word.lower()
                if word in words_dict:
                    words_dict[word] += 1
                else:
                    words_dict[word] = 1
                for letter in word:
                    if letter in symbols_dict:
                        symbols_dict[letter] += 1
                    else:
                        symbols_dict[letter] = 1
    except IOError:
        print "Can't open file '%s'" % (filepath)
    else:
        file.close()


def printStatistic(wlist, slist, status_what):
    print "--------------------------------------------------------------------"
    print "Most common words in '%s'" % (status_what)
    words_list = sorted(wlist.items(), key=lambda x:x[1], reverse=True)
    i = 0
    for item in words_list:
        i += 1
        if i > 10:
            break
        print "%s - %d" % (item[0], item[1])

    print "Most common symbols in '%s'" % (status_what)
    letters_list = sorted(slist.items(),
            key=lambda x:x[1], reverse=True)
    i = 0
    for item in letters_list:
        i += 1
        if i > 10:
            break
        print "%s - %d" % (item[0], item[1])
    print "--------------------------------------------------------------------"

def printStatisticToFile(wlist, slist, status_what, output_file):
    with open(output_file, 'a') as file:
        file.write("------------------------------------------------------------------\n")
        file.write("Most common words in '%s'\n" % (status_what))
        words_list = sorted(wlist.items(), key=lambda x:x[1], reverse=True)
        i = 0
        for item in words_list:
            i += 1
            if i > 10:
                break
            file.write("%s - %d\n" % (item[0], item[1]))

        file.write("Most common symbols in '%s'\n" % (status_what))
        letters_list = sorted(slist.items(),
                key=lambda x:x[1], reverse=True)
        i = 0
        for item in letters_list:
            i += 1
            if i > 10:
                break
            file.write("%s - %d\n" % (item[0], item[1]))
        file.write("------------------------------------------------------------------\n")


def printPathStatus(path):
    print "Path '%s' information:" % (path)
    file_path = ""
    total_words_dict = {}
    total_symbols_dict = {}
    for file in os.listdir(path):
        file_path = path
        if not path.endswith('/'):
            file_path += "/"
        file_path += file
        if os.path.isfile(file_path):
            words_dict = {}
            symbols_dict = {}
            print "Checking file '%s'" % (file_path)
            countFileData(file_path, words_dict, symbols_dict)
            printStatisticToFile(words_dict, symbols_dict, file_path, OUTPUT_FILE_PATH)
            total_words_dict = {k: total_words_dict.get(k, 0) +
                    words_dict.get(k, 0) for k in set(total_words_dict)
                    | set(words_dict)}
            total_symbols_dict = {k: total_symbols_dict.get(k, 0) +
                    symbols_dict.get(k, 0) for k in set(total_symbols_dict)
                    | set(symbols_dict)}
    printStatistic(total_words_dict, total_symbols_dict, path)

if len(sys.argv) > 1:
    if os.path.isdir(sys.argv[1]):
        printPathStatus(sys.argv[1])
        print "Individual file information printed to '%s'" % (OUTPUT_FILE_PATH)
    else:
        print "Not a path"
else:
    print "No path specified"
