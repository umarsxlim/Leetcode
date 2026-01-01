# Last updated: 1/1/2026, 10:53:43 PM
class Solution(object):
    def countNegatives(self, grid):
        c = 0

        for i in grid:
            for j in i:
                if j < 0:
                    c += 1
        
        return c