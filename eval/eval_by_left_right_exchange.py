# -*- coding:utf-8 -*-#


left4 = ['1', 'q', 'a', 'z']
left3 = ['2', 'w', 's', 'x']
left2 = ['3', 'e', 'd', 'c']
left1 = ['4', 'r', 'f', 'v', '5', 't', 'g', 'b']
left = left1 + left2 + left3 + left4

right1 = ['6', 'y', 'h', 'n', '7', 'u', 'j', 'm']
right2 = ['8', 'i', 'k', ',']
right3 = ['9', 'o', 'l', '.']
right4 = ['0', 'p', ';', '/']
right = right1 + right2 + right3 + right4


def eval_by_left_right_exchange(code_table, train_text):
    code = ''
    # print chardet.detect(train_text)
    for ch in train_text:
        if ch in code_table:
            code += code_table[ch]
    new_code = ''
    for ch in code:
        if ch in left:
            new_code += '0'
        if ch in right:
            new_code += '1'
    change_time = 0.0
    last = 0
    for ch in new_code:
        if ch != last:
            change_time += 1
            last = ch
    #print("Evaluating by [2] left-right exchange frequency:")
    # print("    The left-right exchange frequency is %f " % change_time /
    # len(new_code)))
    return change_time / len(new_code)
