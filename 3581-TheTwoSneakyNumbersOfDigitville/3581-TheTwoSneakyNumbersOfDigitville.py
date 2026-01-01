# Last updated: 1/1/2026, 10:53:16 PM
class Solution(object):
    def getSneakyNumbers(self, nums):
        sneaky = []
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                sneaky.append(nums[i])
        return sneaky


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        