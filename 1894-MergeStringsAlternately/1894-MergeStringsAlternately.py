# Last updated: 1/1/2026, 10:53:31 PM
class Solution(object):
    def mergeAlternately(self, word1, word2):

        list1 = list(word1)
        list2 = list(word2)
        ans = ""


        if len(list1) == len(list2):
            for i in range(len(list1)):
                ans += list1[i]
                ans += list2[i]
            
            return ans
        
        elif len(list2) > len(list1):
            over = len(list2) - len(list1)
            for i in range(len(list1)):
                ans += list1[i]
                ans += list2[i]
            for j in range(over, 0, -1):
                ans += list2[-j]
            
            return ans
        
        elif len(list1) > len(list2):
            over = len(list1) - len(list2)
            for i in range(len(list2)):
                ans += list1[i]
                ans += list2[i]
            for j in range(over, 0, -1):
                ans += list1[-j]
            
            return ans