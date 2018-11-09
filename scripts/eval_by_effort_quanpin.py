# -*- coding:utf-8 -*-#
import read_code_table_and_train_text as r
import layout as lyt


def eval_layout_LUTP_effort(LUTP):
    code_table = r.readfile("..\\data\\quanpin_code_table.csv")
    train_text = r.load_test("..\\data\\train_text.txt")
    quanpin_code = list(set(code_table.values()))

    quanpin_code_effort_table = cal_effort(quanpin_code, LUTP)

    quanpin_code_frequency_table = cal_frequency(quanpin_code, train_text, code_table)

    effort = 0.0
    for i in range(len(quanpin_code)):
        effort += quanpin_code_effort_table[quanpin_code[i]] * quanpin_code_frequency_table[quanpin_code[i]]

    return effort


def cal_frequency(quanpin_code, train_text, code_table):
    quanpin_code_frequency_table = dict.fromkeys(quanpin_code, 0)
    for ch in train_text:
        if ch in code_table:
            quanpin_code_frequency_table[ch] += 1
    return quanpin_code_frequency_table


def cal_effort(quanpin_code, LUTP):
    quanpin_code_effort_table = dict.fromkeys(quanpin_code, 0)
    layout = lyt.Layout(LUTP)

    return quanpin_code_effort_table
