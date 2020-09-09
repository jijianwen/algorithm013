class Solution(object):
    # Divide and Conquer
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get(nums, l, r):
            if l == r: return nums[l], nums[l], nums[l], nums[l]
            mid = l + (r-l) // 2

            l_lsum, l_rsum, l_msum, l_asum = get(nums, l, mid)
            r_lsum, r_rsum, r_msum, r_asum = get(nums, mid + 1, r)

            isum = l_asum + r_asum
            lsum = max(l_lsum, l_asum + r_lsum)
            rsum = max(r_rsum, r_asum + l_rsum)
            msum = max(max(l_msum, r_msum), l_rsum + r_lsum)
            return lsum, rsum, msum, isum

        a, b, c, d = get(nums, 0, len(nums) -1)
        return c

    # Greedy
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -sys.maxsize - 1
        curr = ans = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            ans = max(curr, ans)
        return ans

