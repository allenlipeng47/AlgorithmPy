class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hm1, hm2 = {}, {}
        for (ch1, ch2) in zip(s, t):
            if hm1.get(ch1, None) == ch2:
                continue
            if ch1 not in hm1 and ch2 not in hm2:
                hm1[ch1] = ch2
                hm2[ch2] = ch1
            else:
                return False
        return True

s = Solution()
print (s.isIsomorphic("egg", "add"))
print (s.isIsomorphic("foo", "bar"))
print (s.isIsomorphic("paper", "title"))