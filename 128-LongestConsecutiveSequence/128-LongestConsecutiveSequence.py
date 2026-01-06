# Last updated: 1/6/2026, 5:34:03 PM
class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        save = []
        c = 1

        if len(nums) == 0:
            return 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue

            elif nums[i] - nums[i-1] == 1:
                c += 1
            
            else:
                save.append(c)
                c = 1

        save.append(c)
        
        return max(save)