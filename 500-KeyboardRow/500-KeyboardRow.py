# Last updated: 1/1/2026, 10:53:46 PM
class Solution(object):
    def findWords(self, words):
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        returnrow = []

        for i in words:
            letters = list(i.lower())
            flag = True

            if letters[0] in row1:
                setrow = row1
            elif letters[0] in row2:
                setrow = row2
            else:
                setrow = row3

            for j in letters:
                if j not in setrow:
                    flag = False
                    break

            if flag == True:
                returnrow.append(i)

        return returnrow