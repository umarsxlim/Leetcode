# Last updated: 1/14/2026, 4:43:50 PM
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxsum = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows - 2):
            for j in range(cols - 2):
                
                sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                
                if sum > maxsum:
                    maxsum = sum
                    
        return maxsum