# Last updated: 1/1/2026, 10:53:38 PM
class Solution(object):
    def maximumWealth(self, accounts):
        wealthiest = 0
        for i in accounts:
            wealth = 0
            for j in i:
                wealth += j

            if wealth >= wealthiest:
                wealthiest = wealth
        return wealthiest

        