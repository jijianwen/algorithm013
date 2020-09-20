# https://leetcode-cn.com/problems/reverse-bits
class Solution:
    # @param n, an integer
    # @return an integer
    # Time Complexity: O(1). Though we have a loop in the algorithm, the number 
    # of iteration is fixed regardless the input, since the integer is of 
    # fixed-size (32-bits) in our problem.
    # Space Complexity: O(1)
    def reverseBits(self, n):
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n = n >> 1
            power -= 1
        return res
