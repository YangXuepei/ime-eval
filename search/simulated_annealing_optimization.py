# -*- coding:utf-8 -*-#
import random
import math
from helper import *

# Note that this python file should be totally blinded with any practical details, for generic purpose.

#IN: domain specification, cost function
#OUT: current best configuration and its cost
#cost function takes a configuration as input and output its score.

def simulated_annealing(domain, costfunc):
    #generate random initial configuration
    config = []
    for i in range(len(domain)):
        config.append(random.randint(domain[i][0], domain[i][1]))

    best_config = config

    # initial annealing temperature and cooling factor
    annealing_temperature = 10000.0
    cooling_factor = 0.95

    COUNT = 0

    #compare current configuration with its neighbors, substitute it with superior neighbor, if any.
    #until no better neighbor is found.
    while annealing_temperature > 0.1:
        best_config = compare_with_one_neighbor(best_config, domain, costfunc, annealing_temperature)
        annealing_temperature *= cooling_factor
        COUNT += 1
        #print("Current best config: ", best_config, "min cost: ", costfunc(best_config))
    print COUNT
    return best_config


def compare_with_one_neighbor(config, domain, costfunc, annealing_temperature):
    best_config = config
    min_cost = costfunc(config)
    neighbor = generate_neighbors(config, domain)[0]
    neighbor_cost = costfunc(neighbor)
    tolerance_probability = pow(math.e, -(neighbor_cost - min_cost)/ annealing_temperature)
    if neighbor_cost <= min_cost or random.random() < tolerance_probability: #Note that we allow shifting to neighbor even if the cost are equal.
        min_cost = neighbor_cost
        best_config = neighbor
        #print("Found better neighbor: ", best_config, "Cost: ", min_cost)
    return best_config, min_cost

