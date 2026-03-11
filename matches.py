class Solution(object):
    def findWinners(self, matches):
        from collections import defaultdict

        loss_count = defaultdict(int)
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)  
            loss_count[loser] += 1

        no_loss = []
        one_loss = []

        for p in players:
            if loss_count[p] == 0:
                no_loss.append(p)
            elif loss_count[p] == 1:
                one_loss.append(p)

        return [sorted(no_loss), sorted(one_loss)]


obj = Solution()
print(obj.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))