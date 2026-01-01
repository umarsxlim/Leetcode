# Last updated: 1/1/2026, 10:53:33 PM
class Solution(object):
    def diagonalSum(self, mat):
        primary = 0
        secondary = 0
        count = 0
        for i in mat: # primary
            primary += i[count]
            count += 1

        count = len(mat) - 1

        for i in mat: # secondary
            secondary += i[count]
            count -= 1
        
        mid = 0
        if len(mat) % 2 != 0:
            mid = len(mat) // 2
            return primary + secondary - mat[mid][mid]
            
        else:
            return primary + secondary

        """
        :type mat: List[List[int]]
        :rtype: int
        """
        