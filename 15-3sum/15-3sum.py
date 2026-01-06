# Last updated: 1/6/2026, 11:59:18 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                threesum = val + nums[left] + nums[right]

                if threesum == 0:
                    res.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif threesum > 0:
                    right -= 1
                
                elif threesum < 0:
                    left += 1
                
        return res