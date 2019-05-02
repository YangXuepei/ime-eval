# -*- coding:utf-8 -*-#
import csv
import eval_by_avg_length as al
import eval_by_left_right_exchange as lr
import eval_by_effort_naive as ee


def eval(code_table, train_text, character_frequency):
    result = []
    result.append(al.eval_by_avg_length(code_table, character_frequency))
    result.append(lr.eval_by_left_right_exchange(code_table, train_text))
    result.append(ee.eval_by_effort_naive(code_table, train_text))
    return result


def show_options():
    print('')
    print("We have evaluation standards:")
    print("    [1] average code length")
    print("    [2] left-right exchange frequency")
    print("    [3] effort")
