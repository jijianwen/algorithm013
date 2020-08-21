# https://leetcode.com/problems/valid-perfect-square
class Solution(object):
    # Time complexity: O(logN)
    # Space comlexity: O(1)
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r * r > num:
            r = (r + num/r)/2

        return r*r == num

    # Time complexity: O(logN)
    # Space complexity: O(1)
    def isPerfectSquare1(self, num):
        if num == 0: return True

        left, right = 1, num
        while left <= right:
            mid = left + (right - left)//2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1

        return False

