class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        Max = max(nums)

        Result = []

        


        for i in range(len(nums)):
            
            if nums[i] == Max:
                Result.append(-1)
            else:
                i2 = 0 
                for i1 in range (len(nums)):
                    if nums[i+i2] > nums[i]:
                        Result.append(nums[i+i2])
                        break
                    
                    i2+=1
                    if i2 + i == len(nums):
                            i2 = -i
            
              
        return Result
