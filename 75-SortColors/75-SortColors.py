# Last updated: 1/14/2026, 4:44:20 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        

        for i in range(1, len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
