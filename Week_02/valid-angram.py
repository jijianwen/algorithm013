class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        else:
            return collections.Counter(s) == collections.Counter(t)

    # Time complexity:  O(N)
    # Space complexity: O(1)
    def isAnagram1(self, s, t)
        dic = collections.defaultdict(int)
        for item in s: dic[item] += 1
        for item in t: dic[item] -= 1
        return all(x == 0 for x in dic.values())
