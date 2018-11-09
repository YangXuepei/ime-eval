# -*- coding:utf-8 -*-#
from enum import Enum

#domain list that specifies the domain of every elements of LUTP format.
domain = [[1, 26-i] for i in range(26)]

#26 English letters sorted based on their frequency in Chinese writing
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

r = range(1,27)


class Hand(Enum):
    left = 0
    right = 1


class Row(Enum):
    top = 0
    home = 1
    bottom = 2

class Finger(Enum):
    index = 0
    mid = 1
    ring = 2
    pinky = 3

class Key:
    def __init__(self, hand, row, finger):
        self.hand = hand
        self.row = row
        self.finger = finger

# class Key(Enum):
#     K1 = Key()
#     K2 = Key()


class Layout:
    def __init__(self, LUTP):
        self.mapping = {}
        self.LUTP = LUTP
        for i in range(26):
            key = letters[i]
            position = r[LUTP[i]-1]
            r.remove(position)
            self.mapping[key] = position



    def is_complete(self):
        if len(self.mapping) == 26:
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


def test():
    a = [1 for i in range(26)]
    t = Layout(a)
    t.print_layout()
    print t.is_complete()
    print(t.mapping['a'])

#test()
