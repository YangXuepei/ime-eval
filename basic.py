# -*- coding:utf-8 -*-#
import csv
import chardet
import eval_by_avg_length
import eval_by_left_right_exchange



def eval(codedir, testdata, eval_standard):
    switchers = {
        '1': eval_by_avg_length.eval_by_avg_length,
        '2': eval_by_left_right_exchange.eval_by_left_right_exchange
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