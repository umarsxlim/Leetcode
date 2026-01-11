# Last updated: 1/11/2026, 12:36:45 PM
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        c = 0

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < target:
                c += right - left
                left += 1

            else:
                right -= 1
        
        return c