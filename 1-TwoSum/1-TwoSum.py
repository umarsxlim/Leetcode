# Last updated: 1/1/2026, 10:53:56 PM
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                        






#for i in range(len(nums) - 1):
            #if nums[i] == target:
            #    break
           # else:
             #   if nums[i] + nums[i+1] == target:
             #       return(i, i+1)