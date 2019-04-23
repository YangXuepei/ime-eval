# -*- coding:utf-8 -*-#
import read_code_table_and_train_text as r
import layout as lyt

all_pinyin = r.load_all_pinyin("..\\data\\all_pinyin.txt")
# 所有unique的拼音组合
key_effort = {
    1: 1,   2: 1,   3: 1,            10: 0.8,   11: 0.8,    12: 0.8,
    4: 1,   5: 0,   6: 1,            13: 0.8,   14: 0,      15: 0.8,
    7: 2,   8: 1.5, 9: 1.5,          16: 1.3,   17: 1.3,    18: 1.8
}


def eval_layout_LUTP_effort(t):

    code_table = r.readfile("..\\data\\quanpin_code_table.csv")
    #train_text = r.load_test("..\\data\\train_text.txt")
    train_character_frequency = r.readfile("..\\data\\character_frequency.csv")

    quanpin_code_effort_table = cal_basic_effort(t)
    quanpin_left_right_effort_table = cal_left_right_effort(t)
    quanpin_code_frequency_table = cal_frequency(
        train_character_frequency, code_table)

    total_effort = 0.0
    basic_effort = 0.0
    for i in range(len(all_pinyin)):
        basic_effort += quanpin_code_effort_table[all_pinyin[i]
                                                  ] * quanpin_code_frequency_table[all_pinyin[i]]

    left_right_effort = 0.0
    for i in range(len(all_pinyin)):
        left_right_effort += quanpin_left_right_effort_table[all_pinyin[i]
                                                             ] * quanpin_code_frequency_table[all_pinyin[i]]

    total_effort = basic_effort + left_right_effort

    return total_effort


def cal_frequency(train_character_frequency, code_table):
    quanpin_code_frequency_table = dict.fromkeys(all_pinyin, 0)
    for ch in train_character_frequency:
        if ch in code_table:
            pinyin = code_table[ch]
            quanpin_code_frequency_table[pinyin] += int(
                train_character_frequency[ch])
    return quanpin_code_frequency_table


def cal_basic_effort(l):
    quanpin_code_effort_table = dict.fromkeys(all_pinyin, 0)
    mapping = l.get_layout()
    for pinyin in all_pinyin:
        # 这里需要处理一下双拼的effort
        # for c in pinyin:
            #key = mapping[c]
            #quanpin_code_effort_table[pinyin] += key_effort[key]
        sheng, yun = find_sheng_yun_key(pinyin)
        sk = mapping[sheng]
        yk = mapping[yun]
        quanpin_code_effort_table[pinyin] += key_effort[sk] + key_effort[yk]

    #print quanpin_code_effort_table
    return quanpin_code_effort_table


def cal_left_right_effort(l):
    quanpin_left_right_effort_table = dict.fromkeys(all_pinyin, 0)
    mapping = l.get_layout()
    for pinyin in all_pinyin:
        sheng, yun = find_sheng_yun_key(pinyin)
        sk = mapping[sheng]
        yk = mapping[yun]
        sh = 0 if sk > 9 else 1
        yh = 0 if yk > 9 else 1
        count = 1 if sh == yh else 0
        quanpin_left_right_effort_table[pinyin] = count

    return quanpin_left_right_effort_table


def find_sheng_yun_key(pinyin):
    s, y = ' ', ' '
    for i in "aeiouv":
        if pinyin[0] == i:
            s = ' '
            y = pinyin
    if s != ' ' and len(pinyin) > 1:
        if pinyin[1] == 'h':
            s = pinyin[0:2]
            y = pinyin[2:]
        else:
            s = pinyin[0]
            y = pinyin[1:]
    return s, y


def eval_by_effort(domain):
    t = lyt.Layout(domain)
    result = eval_layout_LUTP_effort(t)
    return result


def test():
    a = [1, 14, 15, 1, 8, 6, 5, 10, 3, 7, 1, 5, 6, 1, 4, 2, 1, 1]
    print eval_by_effort(a)


# test()
#print find_sheng_yun_key('huang')
