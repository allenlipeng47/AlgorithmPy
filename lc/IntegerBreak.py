class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1] + [0 for i in range(n - 1)]
        for i in range(2, n + 1):
            currMax = 0
            for j in xrange(1, i / 2 + 1):
                currMax = max(currMax, max(dp[j], j) * max(dp[i - j], i - j))
            dp[i] = currMax
        return dp[n]

s = Solution()
print (s.integerBreak(8))










