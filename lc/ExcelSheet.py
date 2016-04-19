class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n > 0:
            n -= 1
            remaining = n % 26
            ans = chr(65 + remaining) + ans
            n /= 26
        return ans

    def convertToTitle2(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.convertToTitle2((n - 1) / 26) + chr(65 + (n - 1) % 26) if n > 0 else ''


s = Solution()
ans = s.convertToTitle2(27)
print (ans)