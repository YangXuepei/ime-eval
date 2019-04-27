# -*- coding:utf-8 -*-#
from enum import Enum

# domain list that specifies the domain of every elements of LUTP format.
domain = [[1, 18 - i] for i in range(18)]

# 26 English letters
#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#combination = ['i','a','n','e','u','h','o','g','d','s','zy','lj','bw','xm','tc','kq','rf','pv']
#只要在这里填上相应的组合就好, 就能测出最好的18键位layout
combination = [['h','p','a','ua'], ['sh','en','in'], ['zh','ang','iao'], ['b','ao','iong'], ['x','o','v','uai','uan'],['m','s','ie'],
               ['l','ai','ue'], ['d','u'], ['y','eng','ing'], ['w','z','e'], ['j','k','i'], ['n','r','an'],
               ['ch','iang','ui'], ['q', ' ','ian','uang'], ['g','ei','un'], ['c','iu','ou'], ['t','er','ong'], ['f','ia','uo']]

r = range(1, 19)


class Layout:
    def __init__(self, LUTP):
        self.mapping = {}
        self.LUTP = LUTP
        temp = {}
        r = range(1, 19)
        for i in range(18):
            #key = combination[i]
            position = r[LUTP[i] - 1]
            r.remove(position)
           # temp[key] = position
            temp[i] = position
        for i in temp.keys():
            for j in combination[i]:
                self.mapping[j] = temp[i]
        #print self.mapping

    def is_complete(self):
        if len(self.mapping) == 18:
            return True
        else:
            return False

    def add_key(self, letter, key):
        if letter not in self.mapping:
            self.mapping[letter] = key

    def exchange_key(self, letterA, letterB):
        if letterA in self.mapping and letterB in self.mapping:
            tmp = self.mapping[letterA]
            self.mapping[letterA] = self.mapping[letterB]
            self.mapping[letterB] = tmp

    def print_layout(self):
        print self.mapping

    def get_layout(self):
        return self.mapping

    def print_LUPT(self):
        print self.LUTP


def test():
    a = [14, 5, 5, 9, 8, 1, 2, 2, 3, 4, 1, 3, 3, 2, 2, 2, 2, 1]
    t = Layout(a)
    s = str(t.get_layout())
    print s
   # t.print_LUPT()


# test()
