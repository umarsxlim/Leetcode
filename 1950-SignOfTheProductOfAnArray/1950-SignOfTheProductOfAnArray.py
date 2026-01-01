# Last updated: 1/1/2026, 10:53:29 PM
class Solution(object):
    def arraySign(self, nums):
        x = 1
        for i in nums:
            x *= i
            
        if x > 0:
            return 1
        elif x < 0:
            return -1
        elif x == 0:
            return 0