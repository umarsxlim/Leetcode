# Last updated: 1/15/2026, 10:21:24 PM
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        p = 0
        t = 0
        c = 0

        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                c += 1
                p += 1
                t += 1
            
            else:
                t += 1

        return c