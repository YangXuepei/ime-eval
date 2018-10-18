# -*- coding:utf-8 -*-#
import basic as b
import read_code_and_testdata as r


code_dir = r.readfile("testdata.csv")
test_data = r.load_test("test.txt")
eval_type = None
while eval_type != "q":
    if eval_type is not None:
        b.eval(code_dir, test_data, eval_type)
    b.show_options()
    eval_type = raw_input("Please choose a evaluation standard: ")