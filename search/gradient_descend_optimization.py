# -*- coding:utf-8 -*-#
import random
import eval.layout as lyt
from neighbor_generator import *

# Note that this python file should be totally blinded with any practical details, for generic purpose.
# IN: domain specification, cost function
# OUT: current best configuration and its cost
# cost function takes a configuration as input and output its score.


def gradient_descend(domain, costfunc):
    # generate random initial configuration
    config = []
    cost_list = []
    for i in range(len(domain)):
        config.append(random.randint(domain[i][0], domain[i][1]))

    best_config_before_run = config
    best_config_after_run, cost_list = compare_with_neighbors(
        best_config_before_run, domain, costfunc, cost_list)

    # compare current configuration with its neighbors, substitute it with superior neighbor, if any.
    # until no better neighbor is found.
    while best_config_after_run != best_config_before_run:
        best_config_before_run = best_config_after_run
        best_config_after_run, cost_list = compare_with_neighbors(
            best_config_before_run, domain, costfunc, cost_list)
        #print("Current best config: ", best_config_after_run, "min cost: ", costfunc(best_config_after_run))
    return best_config_after_run, cost_list


def compare_with_neighbors(config, domain, costfunc, cost_list):
    best_config = config
    min_cost = costfunc(config)
    for neighbor in generate_neighbors(config, domain):
        t = lyt.Layout(neighbor)
        # t.print_LUPT()
        neighbor_cost = costfunc(neighbor)
        # Note that we allow shifting to neighbor even if the cost are equal.
        if neighbor_cost < min_cost:
            min_cost = neighbor_cost
            best_config = neighbor
            cost_list.append(min_cost)
            print "-----------------------------------------------------"
            print "Found a better neighbor: "
            print "   config is   ", best_config
            print "   cost is     ", min_cost
    return best_config, cost_list
