class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n1 = list()  
        #nums.sort()

        for i in range(len(nums)):
            element = nums[i]
            for j in range (len(nums)): 
                if j == i:
                    continue
                if nums[i] == nums[j]:
                    print(f"nums[i] : {nums[i]} , i : {i}")
                    print(f"nums[j] : {nums[j]} , j : {j}")
                    if nums[i] != i + 1:
                        print(f"nums[i] : {nums[i]} , i : {i}")
                        return [nums[i],i+1]     
                    if nums[j] != j + 1:
                        print(f"nums[j] : {nums[j]} , j : {j}")
                        return [nums[j],j+1]