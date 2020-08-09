class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            u2, u3, u5 = nums[a] * 2, nums[b] * 3, nums[c] * 5
            minval = min(u2, u3, u5)
            if minval == u2:
                a += 1
            if minval == u3:
                b += 1
            if minval == u5:
                c += 1
            nums[i] = minval

        return nums[-1]
