# -*- coding:utf-8 -*-#
# 平均每个字敲击键盘次数



def eval_by_avg_length(code_table, train_text):
    length = 0.0
    sum = 0.0
    # print chardet.detect(train_text)
    for ch in train_text:
        if ch in code_table:
            length += len(code_table[ch])
            sum += 1
    print("Evaluating by [1] average code length:")
    print("    The average code length is %f" % (length / sum))
