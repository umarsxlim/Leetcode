# Last updated: 1/14/2026, 4:43:47 PM
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index = 0
        one = 0

        for i in range(len(mat)):
            c = 0
            for j in mat[i]:
                if j == 1:
                    c += 1
            
            if c > one:
                one = c
                index = i
        
        return [index, one]
