class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j += 1
        return j + 1
