class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candicate = None
        count = 0
        for num in nums:
            if count == 0:
                candicate = num
                count = 1

            elif num == candicate:
                count += 1
            else:
                count -= 1
        return candicate            