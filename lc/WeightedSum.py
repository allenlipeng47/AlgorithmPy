import types

class Solution(object):

    def weightedSum(self, list):
        ans = [0]
        self.weightedSumHelper(l, 1, ans)
        return ans[0]

    def weightedSumHelper(self, l, depth, ans):
        for ele in l:
            if isinstance(ele, list):
                self.weightedSumHelper(ele, depth + 1, ans)
            else:
                ans[0] += ele * depth

s = Solution()
l = [[1, 1], 2, [1, 1]]
ans = s.weightedSum(list)
print (ans)