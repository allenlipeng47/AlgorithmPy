class Solution(object):
    def isHappy1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hm = {}
        while n not in hm:
            hm[n] = 0
            num = 0
            while n > 0:
                num += (n % 10) ** 2
                n /= 10
            if num == 1:
                return True
            n = num
        return False

    # O(1) space by Floyd cycle detection
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n, self.next(n)
        while slow != fast:
            slow = self.next(slow)
            fast = self.next(fast)
            fast = self.next(fast)
        if slow == 1:
            return True
        return False

    def next(self, n):
        num = 0
        while n > 0:
            num += (n % 10) ** 2
            n /= 10
        return num


s = Solution()
print (s.isHappy(19))
