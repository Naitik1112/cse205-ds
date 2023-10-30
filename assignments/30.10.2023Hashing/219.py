class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        elements = {}
        for i in range(len(nums)):
            if nums[i] not in elements:
                elements[nums[i]] = i
            elif nums[i] in elements and abs(i-elements[nums[i]]) <= k:             
                return True
            if nums[i] in elements:
                elements[nums[i]] = i   
        return False           