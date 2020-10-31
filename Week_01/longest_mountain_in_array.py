class Solution:
    def longestMountain(self, A: List[int]) -> int:
        max_len = 0
        for i in range(1, len(A)-1):
            l = r = i
            if A[i-1] < A[i] and A[i] > A[i+1]:
                while l-1 >= 0 and A[l] > A[l-1]:
                    l -= 1
                while r + 1 < len(A) and A[r] > A[r+1]:
                    r += 1
                max_len = max(max_len, r - l + 1)
        return max_len
