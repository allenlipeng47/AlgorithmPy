class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        str = '{0:032b}'.format(n)
        str = str[::-1]
        return int(str, 2)

s = Solution()
n = 6
print (s.reverseBits(6))
# a = '00111'
# print (int(a, 2))