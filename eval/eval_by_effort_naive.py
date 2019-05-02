# -*- coding:utf-8 -*-#
# 当量评估
key_effort = {
    'a': 0.5,
    's': 0.4,
    'd': 0.3,
    'f': 0.2,
    'g': 0.6,
    'h': 0.6,
    'j': 0.2,
    'k': 0.3,
    'l': 0.4,
    ';': 0.5,
    'z': 1.5,
    'x': 1.4,
    'c': 1.3,
    'v': 1.2,
    'b': 1.6,
    'n': 1.5,
    'm': 1.5,
    'q': 1.5,
    'w': 1.4,
    'e': 1.3,
    'r': 1.2,
    't': 1.6,
    'y': 1.6,
    'u': 1.2,
    'i': 1.3,
    'o': 1.4,
    'p': 1.5,
    '_': 2.5,
    '/': 3,
    '.': 1.7,
    ',': 1.6
}


def eval_by_effort_naive(code_table, train_text):
    code = ''
    sum = 0.0
    num = 0
    # print chardet.detect(train_text)
    for ch in train_text:
        if ch in code_table:
            code += code_table[ch]
            num += 1
    for i in code:
        sum += key_effort[i]
    #print("Evaluating by [3] effort:")
    #print('     The sum effort per character is %f' % (sum / num))
    return sum/num
