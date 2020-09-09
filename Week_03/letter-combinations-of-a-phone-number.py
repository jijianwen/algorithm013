class Solution(object):
    # Time complexity:  O(3^N * 4^M)
    # Space complexity: O(3^N * 4^M)
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        m = {
             '2':'abc', '3':'def', '4':'ghi',
             '5':'jkl', '6':'mno', '7':'pqrs',
             '8':'tuv', '9':'wxyz'
        }

        ans = []

        def dfs(i, digits, comb, m):
            if i == len(digits):
                ans.append(comb)
                return

            string = m[digits[i]]
            for c in string:
                dfs(i+1, digits, comb + c, m)

        if digits:
            dfs(0, digits, "", m)
        return ans
