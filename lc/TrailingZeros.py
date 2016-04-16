class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n <= 0 else n / 5 + self.trailingZeroes(n / 5);

    def trailingZeroes2(self, n):
        ans = 0
        while n >= 0:
            ans += n / 5
            n /= 5
        return ans