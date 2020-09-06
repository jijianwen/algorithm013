# https://leetcode.com/problems/decode-ways/
class Solution(object):
    # Time complexity:  O(N)
    # Space complexity: O(N)
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0': return 0
        dp = [1] * len(s)

        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            elif s[i-1] == '1' or (s[i-1] == '2' and '1' <= s[i] <= '6'):
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]

        return dp[-1]
