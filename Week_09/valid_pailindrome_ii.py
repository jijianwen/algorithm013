class Solution(object):
    # Time complexity:  O(N)
    # Space complexity: O(1)
    def pailndrome(self, i, j, s):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.pailndrome(i+1, j, s) or self.pailndrome(i, j-1, s)
        return True
