# Last updated: 1/6/2026, 5:34:00 PM
class Solution(object):
    def moveZeroes(self, nums):
        left = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp
                left += 1