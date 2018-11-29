import unittest

from gradient_descend_optimization import gradient_descend as gd
from simulated_annealing_optimization import simulated_annealing as sa

class Test_optimization(unittest.TestCase):
    def test_gd_rank(self):
        domain = [[1,6] for i in range(5)]
        def costfunc(config):
            return sum(config)
        result = gd(domain, costfunc)
        self.assertEquals(result[0], [1]*5)

    def test_sa_rank(self):
        domain = [[1, 6] for i in range(5)]
        def costfunc(config):
            return sum(config)
        result = sa(domain, costfunc)
        self.assertEquals(result[0], [1] * 5)

if __name__ == '__main__':
    unittest.main()