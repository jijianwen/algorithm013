class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def _combine(first, curr):
            if k == len(curr):
                res.append(curr[:])
                return

            for i in range(first, n+1):
                curr.append(i)
                _combine(i+1, curr)
                curr.pop()

        _combine(1, [])
        return res
