class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def _permute(nums, curr, k):
            if len(curr) == k:
                res.append(curr[:])
                return

            for i in nums:
                if i not in curr:
                    curr.append(i)
                    _permute(nums, curr, k)
                    curr.pop()

        _permute(nums, [], len(nums))
        return res

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def _permute(nums, curr):
            if nums == []:
                res.append(curr)
                return

            for i in range(len(nums)):
                _permute(nums[:i] + nums[i+1:], curr + [nums[i]])

        _permute(nums, [])
        return res
