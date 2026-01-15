# Last updated: 1/15/2026, 9:29:38 PM
class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        res = [0] * n
        
        posindex = 0
        negindex = 1
        
        for i in nums:
            if i > 0:
                res[posindex] = i
                posindex += 2
            else:
                res[negindex] = i
                negindex += 2
                
        return res