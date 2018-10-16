# -*- coding:utf-8 -*-#
import chardet
# 平均每个字敲击键盘次数



def eval_by_avg_length(code_dir, test_data):
    length = 0.0
    sum = 0.0
    # print chardet.detect(test_data)
    for ch in test_data:
        length += len(code_dir[ch])
        sum += 1
    print("Evaluating by [1] average code length:")
    print("    The average code length is %f" % (length / sum))