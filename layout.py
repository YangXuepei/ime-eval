# -*- coding:utf-8 -*-#
from enum import Enum


class Hand(Enum):
    left = 0
    right = 1


class Line(Enum):
    up = 1
    mid = 0
    down = 1


class Key:
    def __init__(self, hand, line, pos):
        self.hand = hand
        self.line = line
        self.pos = pos


class Layout:
    def __init__(self):
        self.map = {}

    def is_complete(self):
        if len(map) == 26:
            return True
        else:
            return False

    def add_key(self, letter, key):
        if not letter in self.map:
            self.map[letter] = key

    def exchangeKey(self, letterA, letterB):
        if letterA in self.map and letterB in self.map:
            tmp = self.map[letterA]
            self.map[letterA] = self.map[letterB]
            self.map[letterB] = tmp


test = Layout()
test.add_key('a', Key(Hand.left, Line.mid, 4))
print(test.map['a'].pos)




