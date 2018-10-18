# -*- coding:utf-8 -*-#
import csv


def readfile(filename):
    csvfile = open(filename, 'rb')
    reader = csv.reader(csvfile)

    result = {}
    for item in reader:
        result[item[0].decode('utf-8')] = item[1]

    csvfile.close()
    # print result
    # return a directory {character:code}
    return result


def load_test(testname):
    # store the testdata in a string
    test = ""
    file = open(testname)
    for line in file.readlines():
        test += line.strip('\n')
    test = test.decode('utf-8')
    return test
