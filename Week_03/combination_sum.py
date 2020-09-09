# https://leetcode.com/problems/combination-sum/
class Solution(object):
    # Time complexity:  O(2^(T/M)), T - target, M - minimal value of candidates
    # Space complexity: O(target)
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(candidates, ans, idx, combine, target):
            if idx == len(candidates):
                return

            if target == 0:
                ans.append(combine)
                return

            dfs(candidates, ans, idx+1, combine, target)

            if target - candidates[idx] >= 0:
                dfs(candidates, ans, idx, combine + [candidates[idx]], target - candidates[idx])

        dfs(candidates, ans, 0, [], target)
        return ans

