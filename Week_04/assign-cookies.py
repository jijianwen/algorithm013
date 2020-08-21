class Solution(object):
    # Time complexity: O(nlog(n), n = max(len(g), len(s)), we used sort()
    # Space complexity: O(1), simple variables used only
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        g.sort()
        s.sort()

        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                j += 1
                i += 1
                res += 1
            else:
                j += 1

        return res
