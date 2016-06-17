class Solution(object):



    def countAndSay(self, n):
        def getNext(nStr):
            i, l = 0, len(nStr)
            ans = ''
            while i < l:
                j = i + 1
                while j < l and nStr[j] == nStr[i]:
                    j += 1
                ans = ans + str(j - i) + nStr[i]
                i = j
            return ans

        ans = '1'
        for i in xrange(n - 1):
            ans = getNext(ans)
        return ans





s = Solution()
print (s.countAndSay(5))