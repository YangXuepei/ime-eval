# -*- coding:utf-8 -*-#
import gradient_descend_optimization as gd
import eval.eval_by_effort_quanpin as ebe
import eval.layout as lyt
#import genetic_optimization as gen
#import simulated_annealing_optimization as sa
#import neural_network_optimization as nn
import sys

print "We have these search methods:"
print "     1. gradient descend optimization"
print "     2. simulated annealing optimization"
print "     3. ..."
search_method = raw_input("Please choose a search method:")
switch = {
    '1': "gd"
}

best_config, min_cost = gd.gradient_descend(lyt.domain, ebe.eval_layout_LUTP_effort)

layout = lyt.Layout(best_config)
layout.print_layout()
print("Cost: ", min_cost, "\n")

# save the best result into local persistent storage.
print "persistent_result"
