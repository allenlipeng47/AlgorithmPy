class Solution(object):
    def titleToNumber2(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = 1
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            ans += (ord(ch) - ord('A') + 1) * base
            base *= 26
        return ans

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y: x * 26 + y, [ord(ch) - ord('A') + 1 for ch in list(s)])


s = Solution()
print (s.titleToNumber('A'));