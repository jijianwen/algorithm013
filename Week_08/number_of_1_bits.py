class Solution(object):
    # Time complexity:  O(1)
    # Space complexity: O(1)
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            n = n & (n-1)
            res += 1
        return res
