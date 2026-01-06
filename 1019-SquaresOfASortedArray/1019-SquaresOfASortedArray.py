# Last updated: 1/6/2026, 11:59:04 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] * nums[left])
                left += 1
            
            else:
                res.append(nums[right] * nums[right])
                right -= 1
        
        res.reverse()
        return res