# http://cherylintcode.blogspot.com/2015/07/longest-substring-with-at-most-k.html
# Solved by hashmap. a practice for python and algorithm

class Solution(object):
    def longestStrKDistinct(self, str, k):
        left, num, ans, hm = 0, 0, 0, {}
        for right in range(len(str)):
            ch = str[right]
            if (ch not in hm or hm[ch] == 0):
                num += 1
                hm[ch] = hm.get(ch, 0) + 1
            while num > k:
                ch = str[left]
                hm[ch] -= 1
                if (hm[ch] <= 0):
                    num -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans