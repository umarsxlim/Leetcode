# Last updated: 1/1/2026, 10:53:30 PM
class Solution(object):
    def truncateSentence(self, s, k):
        words = s.split()
        sentence = ""
        count = 0

        for i in words:
            count += 1            
            if count == k:
                sentence = sentence + i
                break
            else:
                sentence = sentence + i + " "
                
        return sentence