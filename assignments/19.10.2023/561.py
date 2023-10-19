class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        min_res = 0
        nums.sort()
        for i in range(0,len(nums),2):
            print(f"1 : {nums[i+1]} , 2 : {nums[i]}")
            min_res = min_res + min(nums[i+1],nums[i])
        return min_res    