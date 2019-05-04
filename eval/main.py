# -*- coding:utf-8 -*-#
from eval import basic as b
import read_code_table_and_train_text as r

print("we have these tables:")
print("     1. keke five")
print("     2. quanpin")
print("     3. shanren")
print("     4. zhang")
print("     5. 86")
print("     6. xi")
print("     7. quick")
print("     8. daniu")
print("     9. two bi")
print("     10.xifengshou")
print("     11.zheng")
print("     12.xiaohe")

#code_table_type = raw_input("Pleasr choose a code table:")
switch = {
    1: "..\\data\\keke_code_table.csv",
    2: "..\\data\\quanpin_code_table.csv",
    3: "..\\data\\shanren_code_table.csv",
    4: "..\\data\\zhang_code_table.csv",
    5: "..\\data\\86_code_table.csv",
    6: "..\\data\\xi_code_table.csv",
    7: "..\\data\\quick_code_table.csv",
    8: "..\\data\\daniu_double_pinyin_code_table.csv",
    9: "..\\data\\two_bi_code_table.csv",
    10: "..\\data\\xifengshou_code_table.csv",
    11: "..\\data\\zheng_code_table.csv",
    12: "..\\data\\xiaohe_double_pinyin_code_table.csv",

}

result = []
train_text = r.load_test("..\\data\\train_text2.txt")
character_frequency = r.readfile("..\\data\\character_frequency.csv")

for i in range(1, 13):
    code_table = r.readfile(switch.get(i))
    print('=============================================')
    print(switch.get(i)[8:-10])


#eval_type = None
# while eval_type != "q":
#    b.show_options()
#    eval_type = raw_input("Please choose a evaluation standard: ")
#    if eval_type is not None:
#       b.eval(code_table, train_text, eval_type)
    a = b.eval(code_table, train_text, character_frequency)
    result.append(a)

print(result)
a1 = []
a2 = []
a3 = []
for i in result:
    a1.append(i[0])
    a2.append(i[1])
    a3.append(i[2])
print(a1)
print(a2)
print(a3)
