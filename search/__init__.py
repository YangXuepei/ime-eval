# -*- coding:utf-8 -*-#
import gradient_descend_optimization as gd
import eval.eval_by_effort as ebe
import eval.layout as lyt
import time as timestamp
import process_layout as pl
#import genetic_optimization as gen
import simulated_annealing_optimization as sa
#import neural_network_optimization as nn
import sys


print "We have these search methods:"
print "     1. gradient descend optimization"
print "     2. simulated annealing optimization"
print "     3. ..."
search_method = raw_input("Please choose a search method:")
#search_method = 1
switch = {
    '1': "gd",
    '2': "sa"
}

def run(times):
    for time in range(times):
        best_config = gd.gradient_descend(lyt.domain, ebe.eval_by_effort)
        layout = lyt.Layout(best_config).get_layout()
        cost = ebe.eval_by_effort(best_config)


        print "--------------------------------------------------------"
        print "We find the best config:"
        print  best_config
        print "The layout is ", layout
        print "Cost: ", cost
        pl.print_the_layout(layout)

        # save the best result into local persistent storage.

        f = open('..\\data\\persistent_result.txt', 'r')
        last = float(f.readline().strip())
        f.close()

        if cost < last:
            print "This cost is smaller than last persistent result ", last
            f = open('..\\data\\persistent_result.txt', 'w+')
            s = str(best_config)
            f.writelines(str(cost) + '\n')
            f.write(s + '\n')
            f.write(str(layout))
            ts = timestamp.time()
            f.write(str(ts))
            f.close()


run(2)