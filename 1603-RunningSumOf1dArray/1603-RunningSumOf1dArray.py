# Last updated: 1/1/2026, 10:53:35 PM
class Solution(object):
    def runningSum(self, nums):
        run = []
        sum = 0

        for j in nums:
            sum += j
            run.append(sum)
        
        return run

        