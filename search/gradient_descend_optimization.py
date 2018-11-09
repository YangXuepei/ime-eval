# -*- coding:utf-8 -*-#
import random

# Note that this python file should be totally blinded with any practical details, for generic purpose.
# IN: domain specification, cost function
# OUT: current best configuration and its cost
# cost function takes a configuration as input and output its score.


def gradient_descend(domain, costfunc):
    # generate random initial configuration
    config = []
    for i in range(len(domain)):
        config.append(random.randint(domain[i][0], domain[i][1]))

    best_config = config
    min_cost = costfunc(config)

    # compare current configuration with its neighbors, substitute it with superior neighbor, if any.
    # until no better neighbor is found.
    while 1:
        best_config, min_cost = compare_with_neighbors(config, domain, costfunc)
        if best_config == config:
            break
    return best_config, min_cost


def compare_with_neighbors(config, domain, costfunc):
    best_config = config
    min_cost = costfunc(config)
    for neighbor in generate_neighbors(config, domain):
        neighbor_cost = costfunc(neighbor)
        if neighbor_cost <= min_cost:
            # Note that we allow shifting to neighbor even if the cost are equal.
            min_cost = neighbor_cost
            best_config = neighbor
    return best_config, min_cost


def generate_neighbors(config, domain):
    neighbors = []
    for i in range(len(config)):
        mutated = config[i] + random.choice([-1,1])
        if mutated < domain[i][0]:
            mutated = domain[i][0]
        if mutated > domain[i][1]:
            mutated = domain[i][1]

    new_neighbor = config[:i-1].append(mutated).extend(config[i+1:])
    neighbors.append(new_neighbor)
    return neighbors
