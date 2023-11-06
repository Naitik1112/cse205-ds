class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res  = [-1]*len(score)
        for i in range(len(score)):
            val = max(score)
            ind = score.index(val) 
            if i == 0:
                res[ind] = "Gold Medal"
            elif i == 1:
                res[ind] = "Silver Medal" 
            elif i == 2:
                res[ind] = "Bronze Medal"
            else:
                res[ind] = str(i + 1)
            score[ind] = -1
        return res              