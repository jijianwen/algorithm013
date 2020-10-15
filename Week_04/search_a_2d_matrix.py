# https://leetcode.com/problems/search-a-2d-matrix
class Solution(object):
    # Time complexity:  O(logM + LogN)
    # Space complexity: O(1)
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0] : return False

        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        row = min(left, right)

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

