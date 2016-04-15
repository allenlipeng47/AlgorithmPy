class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n, m = len(dungeon), len(dungeon[0])
        dp = [[99999 for i in range(m + 1)] for i in range(n + 1)]
        dp[n][m - 1] = dp[n - 1][m] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                if need <= 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = need
        return dp[0][0]

s = Solution()
l = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]
print (s.calculateMinimumHP(l))