class Solution(object):

    base = 0b11111111111111111111

    # last 3 digit for 'A', 'T', 'C', 'G' are separately 001, 100, 011, 100. They are different.
    # In this way, use 3 bits to symbolize a letter.
    # When encounter the same, use substring to return
    def findRepeatedDnaSequences2(self, s):
        num = 0
        hs = set()
        ans = set()
        for i in range(10):
            num = (num << 3) | (ord(s[i]) & 7)
        hs.add(num)
        for i in range(10, len(s)):
            num = ((num << 3) | (ord(s[i]) & 7)) & 0x3fffffff
            if num in hs:
                ans.add(s[i - 9 : i + 1])
            hs.add(num)
        return list(ans)




    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        num = 0
        ansHm = {}
        hm = {}
        for i in range(10):
            num = self.move(num, s[i])
        hm[num] = 1
        for i in range(10, len(s)):
            num = self.move(num, s[i])
            if num in hm:
                ansHm[num] = 1
            hm[num] = 1
        ans = []
        for i in ansHm.keys():
            ans.append(self.getStr(i))
        return ans


    def move(self, s, ch):
        if ch == 'A':
            return (s << 2) & self.base
        elif ch == 'T':
            return (((s << 2) | 0b01) & self.base)
        elif ch == 'C':
            return (((s << 2) | 0b10) & self.base)
        elif ch == 'G':
            return (((s << 2) | 0b11) & self.base)
        else:
            return None

    def getStr(self, num):
        ans = '';
        for i in range(10):
            value = num & 3
            if value == 0:
                ans = 'A' + ans
            elif value == 1:
                ans = 'T' + ans
            elif value == 2:
                ans = 'C' + ans
            elif value == 3:
                ans = 'G' + ans
            num >>= 2
        return ans


s = Solution()
list = s.findRepeatedDnaSequences2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print (list)
print ('{0:032b}'.format(ord('A')))
print ('{0:032b}'.format(ord('T')))
print ('{0:032b}'.format(ord('C')))
print ('{0:032b}'.format(ord('T')))