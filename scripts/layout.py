# -*- coding:utf-8 -*-#
from enum import Enum

#domain list that specifies the domain of every elements of LUTP format.
domain = [[1, 26-i] for i in range(26)]

#26 English letters sorted based on their frequency in Chinese writing
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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

    def is_complete(self):
        if len(map) == 26:
            return True
        else:
            return False

    def add_key(self, letter, key):
        if not letter in self.map:
            self.map[letter] = key

    # def exchangeKey(self, letterA, letterB):
    #     if letterA in self.map and letterB in self.map:
    #         tmp = self.map[letterA]
    #         self.map[letterA] = self.map[letterB]
    #         self.map[letterB] = tmp

# def print_layout():


def test():
    test = Layout()
    test.add_key('a', Key(Hand.left, Row.mid, 4))
    print(test.map['a'].pos)

#test()
