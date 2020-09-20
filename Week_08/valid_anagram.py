class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        dic_s, dic_t = {}, {}
        for i in range(len(s)):
            dic_s[s[i]] = dic_s.get(s[i], 0) + 1
            dic_t[t[i]] = dic_t.get(t[i], 0) + 1

        return dic_s == dic_t
