class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        arr = 0 
        count = 0 
        for i in nums :
            if i == 1 :
                count+=1
                arr = max(arr , count)
            else:
                count = 0 
        return arr
