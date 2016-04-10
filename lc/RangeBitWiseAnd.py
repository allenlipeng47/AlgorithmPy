class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        move = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            move += 1
        return m << move

s = Solution()
print (s.rangeBitwiseAnd(4, 6))