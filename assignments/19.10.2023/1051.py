class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h1 = list()
        sorted_h1.extend(heights)
        heights.sort()
        count = 0 
        for i in range (len(heights)):
            count = count + 1 if sorted_h1[i] != heights[i] else count
        return count    