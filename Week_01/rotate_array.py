class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k > 0:
            nums[k:len(nums)], nums[0:k] = nums[0:len(nums)-k], nums[len(nums)-k:len(nums)]
