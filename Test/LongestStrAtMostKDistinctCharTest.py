import unittest
from lc.LongestStrAtMostKDistinctChar import Solution

class SolutionTest(unittest.TestCase):


    def test(self):
        s = Solution()
        assert s.longestStrKDistinct('eceba', 2) == 3
        assert s.longestStrKDistinct('eceba', 3) == 4
        assert s.longestStrKDistinct('asdfsag', 3) == 4
        assert s.longestStrKDistinct('asdfsag', 4) == 6
        assert s.longestStrKDistinct('asdfsag', 0) == 0
        assert s.longestStrKDistinct('asdfsag', 1) == 1
        assert s.longestStrKDistinct('asdfsag', 7) == 7
        assert s.longestStrKDistinct('asdfsag', 8) == 7

