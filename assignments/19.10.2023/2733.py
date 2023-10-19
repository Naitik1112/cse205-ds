class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        Num1 = max(nums)
        Num2 = min(nums)

        for i in nums:
            if i != Num1 and i != Num2:
                return i

        return -1        