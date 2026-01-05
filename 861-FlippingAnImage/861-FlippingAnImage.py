# Last updated: 1/5/2026, 4:31:29 PM
class Solution(object):
    def flipAndInvertImage(self, image):
        for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image)):
                if image[i][j] == 0:
                    image[i][j] = 1
                elif image[i][j] == 1:
                    image[i][j] = 0
        
        return image