class Solution(object):
    # Time complexity:  O(1)
    # Space complexity: O(1)
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        return n & (n-1) == 0
