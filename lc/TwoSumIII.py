import unittest


class Solution(object):
    def __init__(self):
        self.hm = {}
        pass

    def add(self, x):
        self.hm[x] = self.hm.get(x, 0) + 1
        pass

    def find(self, x):
        for key, count in self.hm.iteritems():
            expect = x - key
            if key == expect and count >= 2:
                return True
            elif expect in self.hm:
                return True
        return False


class TestSoltuion(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test(self):
        assert self.s.find(1) == False
        self.s.add(1)
        self.s.add(2)
        assert self.s.find(3) == True
        self.s.add(2)
        assert self.s.find(4) == True

    def tearDown(self):
        self.s = None