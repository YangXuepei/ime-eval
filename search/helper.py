# -*- coding:utf-8 -*-#
import random

def generate_neighbors(config, domain):
    return generate_all_neighbors(config, domain)
    # return generate_random_limited_neighbors(config, domain)

def generate_random_limited_neighbors(config, domain):
    neighbors = []
    for i in range(len(config)):
        mutated = config[i] + random.choice([-1,1])
        if mutated < domain[i][0]:
            mutated = domain[i][0]
        if mutated > domain[i][1]:
            mutated = domain[i][1]
        new_neighbor = config[:i] + [mutated] + config[i+1:]
        neighbors.append(new_neighbor)
    return neighbors

def generate_all_neighbors(config, domain):
    neighbors = []
    for i in range(len(config)):
        mutated = config[i] + 1
        if mutated > domain[i][1]:
            mutated = domain[i][1]
        new_neighbor = config[:i] + [mutated] + config[i + 1:]
        neighbors.append(new_neighbor)

        mutated = config[i] - 1
        if mutated < domain[i][0]:
            mutated = domain[i][0]
        new_neighbor = config[:i] + [mutated] + config[i + 1:]
        neighbors.append(new_neighbor)
    return neighbors