class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        if nums[left] <= nums[right]: return nums[left]
        return nums[right]
