class Solution(object):
    # Using Counter
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        conter = collections.Counter(nums)
        return conter.most_common(1)[0][0]

    # Using sort()
    def majorityElement1(self, nums):
        nums.sort()
        return nums[len(nums)//2]

    # Divide and conquer
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def majority(left, right):
            if left == right:
                return nums[left]

            mid = left + (right - left)//2

            lmost = majority(left, mid)
            rmost = majority(mid+1, right)

            if lmost == rmost:
                return lmost

            lcount = sum(1 for i in range(left, right+1) if nums[i] == lmost)
            rcount = sum(1 for i in range(left, right+1) if nums[i] == rmost)

            return lmost if lcount > rcount else rmost

        return majority(0, len(nums) - 1)
