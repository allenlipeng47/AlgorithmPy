# http://www.cnblogs.com/EdwardLiu/p/4306561.html

class Solution(object):

    def reverseWords(self, s):
        s = s + ' '
        ans = ''
        i = 0
        while i < len(s):
            j = s.index(' ', i)
            ans =  ' ' + s[i:j] + ans
            i = j + 1
        ans = ans[1:]
        return ans

s = Solution()
str = "hello the world"
print (s.reverseWords(str))