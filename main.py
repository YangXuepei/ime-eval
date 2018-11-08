# -*- coding:utf-8 -*-#
import basic as b
import read_code_and_testdata as r

print("we have these tables:")
print("     1. keke five ")
print("     2. quanpin ")
code_table_type = raw_input("Pleasr choose a code table:")
switch = {
    '1' : "data\keke_code_table.csv",
    '2' : "data\quanpin_code_table.csv"
}
code_dir = r.readfile(switch.get(code_table_type))
test_data = r.load_test("data\\traintext.txt")

eval_type = None
while eval_type != "q":
    if eval_type is not None:
        b.eval(code_dir, test_data, eval_type)
    b.show_options()
    eval_type = raw_input("Please choose a evaluation standard: ")
