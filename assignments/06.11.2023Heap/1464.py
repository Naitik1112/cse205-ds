class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        val1 = max(nums)
        nums.pop(nums.index(val1))

        val2 = max(nums) 
        return (val1-1)*(val2-1)