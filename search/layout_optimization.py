# -*- coding:utf-8 -*-#
import gradient_descend_optimization as gd
import eval_layout_LUTP_effort from ime-eval.scripts.eval_by_effort
import ime-eval/layout as lyt
#import genetic_optimization as gen
#import simulated_annealing_optimization as sa
#import neural_network_optimization as nn
import sys

if len(sys.argv) == 1:
    algorithm == 'gd'
else:
    algorithm = sys.argv[1]

if algorithm == 'gd':
    best_config, min_cost = gd.gradient_descend(lyt.domain, eval_layout_LUTP_effort.)
elif algorithm == 'gen':
    break
elif algorithm == 'sa':
    break
elif algorithm == 'nn':
    break
else:
    print("Wrong usage.\n")

def print_result(best_config, min_cost):
    layout = lyt.Layout(bset_config)
    layout.print_layout()
    print("Cost: ", min_cost, "\n")

def persistent_result(best_config, min_cost):
    #save the best result into local persistent storage.
