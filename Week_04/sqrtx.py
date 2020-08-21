class Solution:
    # Time complexity: O(logx)
    # Space complexity: O(1)
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return right

    # Time complexity: O(logx)
    # Space compexity: O(1)
    def mySqrt1(self, x):
        if x == 0: return x

        c = x0 = float(x)
        while True:
            xi = 0.5 * (x0 + c/x0)
            if abs(xi - x0) < 1e-6:
                break
            x0 = xi

        return int(x0)

    def mySqrt2(self, x):
        r = x
        while r*r > x:
            r = (r + x/r)/2
        return r
