# -*- coding:utf-8 -*-#

of = open("..\data\quanpin_code_table.txt",'rb')
re = open('..\data\quanpin1_code_table.txt', 'w')
i = 0
for line in of.readlines():
    #print i
    i += 1
    st =line.split()
    re.writelines(st[0] + ',' + st[1] + '\n')

of.close()
re.close()
