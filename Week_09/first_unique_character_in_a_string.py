class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = {}
        for c in s:
            ht[c] = ht.get(c, 0) + 1

        for i in range(len(s)):
            if ht[s[i]] == 1:
                return i
        return -1
