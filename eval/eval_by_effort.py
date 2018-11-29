# -*- coding:utf-8 -*-#
import read_code_table_and_train_text as r
import layout as lyt

all_pinyin = r.load_all_pinyin("..\\data\\all_pinyin.txt")
# 所有unique的拼音组合
key_effort = {
    1: 1,   2: 1,   3: 1,            10: 0.8,   11: 0.8,    12: 0.8,
    4: 1,   5: 0,   6: 1,            13: 0.8,   14: 0,      15: 0.8,
    7: 2,   8: 1.5, 9: 1.5,          16: 1.3,   17: 1.3,    18: 1.8
}

def eval_layout_LUTP_effort(t):

    code_table = r.readfile("..\\data\\quanpin_code_table.csv")
    train_text = r.load_test("..\\data\\train_text.txt")

    quanpin_code_effort_table = cal_basic_effort(t)
    quanpin_left_right_effort_table = cal_left_right_effort(t)
    quanpin_code_frequency_table = cal_frequency(train_text, code_table)
    total_effort = 0.0
    basic_effort = 0.0
    for i in range(len(all_pinyin)):
        basic_effort += quanpin_code_effort_table[all_pinyin[i]] * quanpin_code_frequency_table[all_pinyin[i]]

    left_right_effort = 0.0
    for i in range(len(all_pinyin)):
        left_right_effort += quanpin_left_right_effort_table[all_pinyin[i]] * quanpin_code_frequency_table[all_pinyin[i]]

    total_effort = basic_effort + left_right_effort

    return total_effort


def cal_frequency(train_text, code_table):
    quanpin_code_frequency_table = dict.fromkeys(all_pinyin, 0)
    for ch in train_text:
        if ch in code_table:
            pinyin = code_table[ch]
            quanpin_code_frequency_table[pinyin] += 1
    return quanpin_code_frequency_table


def cal_basic_effort(l):
    quanpin_code_effort_table = dict.fromkeys(all_pinyin, 0)
    mapping = l.get_mapping()
    for pinyin in all_pinyin:
        for c in pinyin:
            key = mapping[c]
            quanpin_code_effort_table[pinyin] += key_effort[key]

    #print quanpin_code_effort_table
    return quanpin_code_effort_table

def cal_left_right_effort(l):
    quanpin_left_right_effort_table = dict.fromkeys(all_pinyin, 0)
    mapping = l.get_mapping()
    for pinyin in all_pinyin:
        count = 0
        last = 0 if mapping[pinyin[0]] > 9 else 1
        for c in pinyin:
            hand = 0 if mapping[pinyin[0]] > 9 else 1
            count += 1 if hand == last else 0
        quanpin_left_right_effort_table[pinyin] = count

    return quanpin_left_right_effort_table


def eval_by_effort(domain):
    t = lyt.Layout(domain)
    print domain
    t.print_layout()
    result =  eval_layout_LUTP_effort(t)
    return result


def test():
    a = [1, 14, 15, 1, 8, 6, 5, 10, 3, 7, 1, 5, 6, 1, 4, 2, 1, 1]
    eval_by_effort(a)

#test()