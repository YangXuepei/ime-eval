# -*- coding:utf-8 -*-#
import basic
import read_code_and_testdata


code_dir = read_code_and_testdata.readfile("testdata.csv")
test_data = read_code_and_testdata.load_test("test.txt")
eval_type = None
while eval_type != "q":
    if eval_type is not None:
        basic.eval(code_dir, test_data, eval_type)
    basic.show_options()
    eval_type = raw_input("Please choose a evaluation standard: ")