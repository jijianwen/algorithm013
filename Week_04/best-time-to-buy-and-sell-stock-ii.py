class Solution(object):
    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprof = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxprof += (prices[i] - prices[i-1])

        return maxprof
