class Solution(object):
    # Time complexity: O(n)
    # Space complexity: O(1)
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_i = 0
        for i, num in enumerate(nums):
            if max_i >= i and i + num > max_i:
                max_i = i + num

        return max_i >= i
