# Last updated: 1/5/2026, 11:48:12 PM
class Solution(object):
    def topKFrequent(self, nums, k):
        unique = []
        counter = []
        c = 1
        nums.sort()

        for i in nums:
            if i not in unique:
                unique.append(i)
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                c += 1
            else:
                counter.append(c)
                c = 1
        counter.append(c)

        res = []
        for i in range(len(counter)):
            for j in range(i + 1, len(counter)):
                if counter[j] > counter[i]:
                    counter[i], counter[j] = counter[j], counter[i]
                    unique[i], unique[j] = unique[j], unique[i]

        for i in range(k):
            res.append(unique[i])

        return res