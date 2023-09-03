class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        i1 = 0 
        for i in nums : 
            if len(str(i))%2 == 0 :
                i1+=1
        return i1