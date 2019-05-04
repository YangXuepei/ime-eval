# -*- coding:utf-8 -*-#
import eval.read_code_table_and_train_text as r
import csv


all_pinyin = r.readfile("..\\data\\quanpin_code_table.csv")
train_character_frequency = r.readfile("..\\data\\character_frequency.csv")

new_table = open('new_table.csv', mode='w')
writer = csv.writer(
    new_table,
    delimiter=',',
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL)

for i in train_character_frequency:
    for j in all_pinyin:
        if i == j:
            print(
                i.encode('utf-8'),
                train_character_frequency[i],
                all_pinyin[i])
            writer.writerow(
                [i.encode('utf-8'), train_character_frequency[i], all_pinyin[i]])
