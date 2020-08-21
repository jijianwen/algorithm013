# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution(object):
    # Time complexity:  O(logN)
    # Space complexity: O(1)
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[-1] > nums[0]: return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
