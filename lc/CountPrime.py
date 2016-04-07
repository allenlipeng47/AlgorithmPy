import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [False, False] + [True for i in range(n - 2)]
        for i in range(2, int(n**0.5) + 1):
            if arr[i] is True:
                arr[i * i :: i] = len(arr[i * i :: i]) * [False]
        return arr.count(True)


s = Solution()
print (s.countPrimes(2))