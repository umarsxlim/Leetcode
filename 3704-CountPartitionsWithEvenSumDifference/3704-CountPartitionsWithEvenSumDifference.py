# Last updated: 1/1/2026, 10:53:14 PM
class Solution(object):
    def countPartitions(self, nums):
        partition = []
        c = 0

        for i in range(len(nums)-1):
            nsum = 0
            psum = 0
            partition.append(nums[0])
            nums.remove(nums[0])

            for i in partition:
                psum += i

            for i in nums:
                nsum += i
            
            if (psum - nsum) % 2 == 0:
                c += 1
        
        return c