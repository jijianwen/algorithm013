class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        def _permuteUnique(nums, curr):
            if nums == []:
                res.append(curr)
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                else:
                    _permuteUnique(nums[:i] + nums[i+1:], curr + [nums[i]])

        _permuteUnique(nums, [])
        return res
