# Last updated: 1/1/2026, 10:53:44 PM
class Solution(object):
    def transpose(self, matrix):
        transpose = []
        
        for i in range(len(matrix[0])):
            col = []
            for j in range(len(matrix)):
                col.append(matrix[j][i])
            transpose.append(col)

        return transpose