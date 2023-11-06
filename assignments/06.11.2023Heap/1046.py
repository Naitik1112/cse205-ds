class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            if stones[-2] == stones[-1]:
                stones.pop(-1)
                stones.pop(-1)
            else:
                stones[-1] = stones[-1] - stones[-2]
                stones.pop(-2)
        return stones[0] if len(stones) == 1 else 0              