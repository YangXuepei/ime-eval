# -*- coding:utf-8 -*-#
import read_code_table_and_train_text as r
import layout as lyt

all_pinyin = r.load_all_pinyin("..\\data\\all_pinyin.txt")
# 所有unique的拼音组合
key_effort = {
    1: 2,
    2: 2,
    3: 2,
    4: 2,
    5: 2,
    6: 3,
    7: 2,
    8: 2,
    9: 2,
    10: 2,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 2,
    16: 2,
    17: 0,
    18: 0,
    19: 0,
    20: 2,
    21: 2,
    22: 2,
    23: 2,
    24: 3.5,
    25: 2,
    26: 2
}

def eval_layout_LUTP_effort(LUTP):
    code_table = r.readfile("..\\data\\quanpin_code_table.csv")
    train_text = r.load_test("..\\data\\train_text.txt")

    quanpin_code_effort_table = cal_effort(LUTP)
    quanpin_code_frequency_table = cal_frequency(train_text, code_table)
    effort = 0.0
    for i in range(len(all_pinyin)):
        effort += quanpin_code_effort_table[all_pinyin[i]] * quanpin_code_frequency_table[all_pinyin[i]]

    return effort


def cal_frequency(train_text, code_table):
    quanpin_code_frequency_table = dict.fromkeys(all_pinyin, 0)
    for ch in train_text:
        if ch in code_table:
            pinyin = code_table[ch]
            quanpin_code_frequency_table[pinyin] += 1
    #print quanpin_code_frequency_table
   # print quanpin_code_frequency_table['wo']
    return quanpin_code_frequency_table


def cal_effort(LUTP):
    quanpin_code_effort_table = dict.fromkeys(all_pinyin, 0)
    l = lyt.Layout(LUTP)
    l.print_layout()
    mapping = l.get_mapping()
    for pinyin in all_pinyin:
        for c in pinyin:
            key = mapping[c]
            quanpin_code_effort_table[pinyin] += key_effort[key]

    print quanpin_code_effort_table
    return quanpin_code_effort_table


def test():
    a = [1 for i in range(0,26)]
    print eval_layout_LUTP_effort(a)

test()