# -*- coding:utf-8 -*-#
import csv
import eval_by_avg_length as al
import eval_by_left_right_exchange as lr


def eval(codedir, testdata, eval_standard):
    switchers = {
        '1': al.eval_by_avg_length,
        '2': lr.eval_by_left_right_exchange
    }
    func = switchers.get(eval_standard)
    func(codedir, testdata)


def show_options():
    print ''
    print("We have evaluation standards:")
    print("    [1] average code length")
    print("    [2] left-right exchange frequency")


def eval_by_(code_dir):
    return 0