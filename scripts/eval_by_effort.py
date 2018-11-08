# -*- coding:utf-8 -*-#
#当量评估
key_effort = {
    'a': 0,
    's': 0,
    'd': 0,
    'f': 0,
    'g': 2,
    'h': 2,
    'j': 0,
    'k': 0,
    'l': 0,
    'z': 2,
    'x': 2,
    'c': 2,
    'v': 2,
    'b': 3.5,
    'n': 2,
    'm': 2,
    'q': 2,
    'w': 2,
    'e': 2,
    'r': 2,
    't': 2,
    'y': 3,
    'u': 2,
    'i': 2,
    'o': 2,
    'p': 2,
}



#def eval_layout_LUTP_effort():


#def eval_layout_effort():

#def eval_key_effort():

#def eval_pinyin_effort():


def eval_by_effort(code_dir, test_data):
    code = ''
    sum = 0.0
    num = 0
    # print chardet.detect(test_data)
    for ch in test_data:
        if ch in code_dir:
            code += code_dir[ch]
            num += 1
    for i in code:
        sum += key_effort[i]
    print("Evaluating by [3] effort:")
    print('     The sum effort per character is %f'%(sum/num))
