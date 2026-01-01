# Last updated: 1/1/2026, 10:53:41 PM
class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                count += 1
        
        return count