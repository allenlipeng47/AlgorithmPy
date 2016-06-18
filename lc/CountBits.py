class Solution(object):
    def countBits(self, num):
        ans = [0]
        for i in range(1, num + 1):
            ans.append(ans[i / 2] + i % 2)
        return ans


s = Solution()
print (s.countBits(2))
for i in range (0, 5):
    print (i)