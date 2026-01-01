# Last updated: 1/1/2026, 10:53:13 PM
class Solution(object):
    def recoverOrder(self, order, friends):
        finishorder = []
        for i in order: # Order 
            for j in friends: # Friends
                if i == j:
                    finishorder.append(i)
        return finishorder
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        