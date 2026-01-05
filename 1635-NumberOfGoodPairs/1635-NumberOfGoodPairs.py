# Last updated: 1/5/2026, 4:31:23 PM
class Solution(object):
    def numIdenticalPairs(self, nums):
        good = 0

        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and i < j:
                    good += 1
        
        return good