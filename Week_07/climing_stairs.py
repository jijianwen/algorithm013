class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        now, nxt = 1, 1
        for i in range(n):
            now, nxt = nxt, now + nxt
 
        return now
