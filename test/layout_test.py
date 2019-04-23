import unittest

from eval.layout import *


class TestLayout(unittest.TestCase):
    def test_init(self):
        l = Layout([18 - i for i in range(18)])
        should_mapping = {}
        for i in range(18):
            should_mapping[combination[i]] = 18 - i

        # print("mapping is ", l.get_mapping())
        # print("should mapping is ", should_mapping)
        self.assertEquals(l.get_mapping(), should_mapping)


if __name__ == '__main__':
    unittest.main()
