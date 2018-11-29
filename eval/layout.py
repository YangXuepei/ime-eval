# -*- coding:utf-8 -*-#
from enum import Enum

#domain list that specifies the domain of every elements of LUTP format.
#domain = [[1, 18-i] for i in range(18)]

#26 English letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

combination = ['i','a','n','e','u','h','o','g','d','s','zy','lj','bw','xm','tc','kq','rf','pv']

r = range(1,19)

print r

class Layout:
    def __init__(self, LUTP):
        self.mapping = {}
        self.LUTP = LUTP
        temp = {}
        for i in range(18):
            key = combination[i]
            position = r[LUTP[i]-1]
            r.remove(position)
            temp[key] = position
        for pair in temp.keys():
            for i in pair:
                self.mapping[i] = temp[pair]
        #print self.mapping

    def is_complete(self):
        if len(self.mapping) == 18:
            return True
        else:
            return False

    def add_key(self, letter, key):
        if not letter in self.mapping:
            self.mapping[letter] = key

    def exchange_key(self, letterA, letterB):
        if letterA in self.mapping and letterB in self.mapping:
            tmp = self.mapping[letterA]
            self.mapping[letterA] = self.mapping[letterB]
            self.mapping[letterB] = tmp

    def print_layout(self):
        print self.mapping

    def get_mapping(self):
        return self.mapping


def test():
    a = [1 for i in range(18)]
    t = Layout(a)
    t.print_layout()

