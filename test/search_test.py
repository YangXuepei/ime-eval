import unittest
import math

from search.gradient_descend_optimization import gradient_descend as gd
from search.simulated_annealing_optimization import simulated_annealing as sa


def costfunc1(config):
    return sum(config)

def costfunc2(config):
    return math.sin(1.0/sum(config))


class Test_optimization(unittest.TestCase):
    # def test_gd_correctness(self):
    #     domain = [[1,6] for i in range(5)]
    #     result = gd(domain, costfunc1)
    #     self.assertEquals(result[0], [6]*5)

    def test_sa_correctness(self):
        domain = [[1, 6] for i in range(5)]
        result = sa(domain, costfunc1)
        self.assertEquals(result[0], [1]*5)

    def test_sa_performance(self):
        domain = [[1, 6] for i in range(5)]
        result = sa(domain, costfunc2)
        self.assertEquals(result[0], [6]*5)

if __name__ == '__main__':
    unittest.main()