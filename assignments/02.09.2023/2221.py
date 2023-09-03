class Solution:
    def triangularSum(self, nums: List[int]) -> int:
       
        def rucc (  arr = [ ] , arr1 = [ ] ):
            if len(arr1) == 1 :
                return arr1[0]
            for i in range (0,len(arr1) -1):
                a = (arr1[i] + arr1[i+1])%10
                arr.append(a)
            return rucc([],arr)
        sum = rucc ([],nums)
        
        return sum 


