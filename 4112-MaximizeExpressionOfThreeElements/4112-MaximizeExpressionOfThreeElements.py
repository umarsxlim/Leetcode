# Last updated: 1/1/2026, 10:53:17 PM
class Solution(object):
    def maximizeExpressionOfThree(self, nums):
        sortednums = sorted(nums)
        a = sortednums[-1]
        b = sortednums[-2]
        c = sortednums[0]

        return a + b - c
        