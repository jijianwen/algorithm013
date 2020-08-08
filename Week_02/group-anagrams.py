class Solution(object):
    # Categroize by sorted string
    # Time Complexity: O(N*KlogK), where N is the length of strs, and K is the 
    # maximum length of a string in strs
    # Space Complexity: O(N*K)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = collections.defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return res.values()
