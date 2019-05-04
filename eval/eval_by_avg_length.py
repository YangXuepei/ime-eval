# -*- coding:utf-8 -*-#
# 平均每个字敲击键盘次数


def eval_by_avg_length(code_table, character_frequency):
    length = 0.0
    sum = 0.0
    # print chardet.detect(train_text)
    for ch in dict.fromkeys(character_frequency, 0):
        if ch in code_table:
            num = int(character_frequency[ch])
            length += len(code_table[ch]) * num
            sum += num
    #print("Evaluating by [1] average code length:")
    #print("    The average code length is %f" % (length / sum))
    return length / sum
