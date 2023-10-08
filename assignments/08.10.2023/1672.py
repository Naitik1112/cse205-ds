class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Rich = 0
        for wealth in accounts:
            Rich = Max(Rich,sum(wealth))
        return Rich    
                