class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        res = [ ]
        while i != 0 :
            if i not in arr :
                print(i)
                res.append(i)
            if len(res) == k:
                break
            i+=1
        s = res.pop()
        return s
        


