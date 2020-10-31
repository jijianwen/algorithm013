class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    res[i] += 1
                elif nums[j] > nums[i]:
                    res[j] += 1
        return res
