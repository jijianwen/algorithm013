class Solution(object):
    # Brute force
    # Time complexity: O(logn)
    # Space complexity: O(1)
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def findmin(nums):
            if len(nums) == 1 or nums[-1] > nums[0]: return 0

            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                if nums[mid] < nums[mid - 1]:
                    return mid

                if nums[mid] > nums[0]:
                    left = mid + 1
                else:
                    right = mid -1

            return None

        if len(nums) == 1: return -1 if nums[0] != target else 0

        mid = findmin(nums)
        if target == nums[mid]:
            return mid
        elif target > nums[mid] and target <= nums[-1]:
            left, right = mid, len(nums) - 1
        else:
            left, right = 0, mid - 1

        while left <= right:
            median = left + (right - left) // 2
            if nums[median] == target:
                return median
            elif nums[median] > target:
                right = median - 1
            else:
                left = median + 1

        return -1

    # Binary search
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid

            if nums[0] <= nums[mid]:
                if target < nums[mid] and target >= nums[0]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
