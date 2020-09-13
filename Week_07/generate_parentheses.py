class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right, res=[]):
            if left: generate(p + '(', left - 1, right)
            if right > left: generate(p + ')', left, right -1)
            if not right: res += p,
            return res

        return generate('', n, n)
