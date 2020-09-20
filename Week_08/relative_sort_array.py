class Solution(object):
    # Time complexity:  O(MlogM + N), M=len(arr1), N=len(arr2)
    # Space complexity: O(M)
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        c = collections.Counter(arr1)
        res = []
        for i in arr2:
            res += [i] * c.pop(i)
        return res + sorted(c.elements())
