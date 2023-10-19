class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = 0
        diff = list()
        for i in range (len(arr)-1):
            diff.append(arr[i+1] - arr[i])
        res = min(diff)    
        final = []
        for i in range (len(arr)-1):
            if arr[i+1] - arr[i] == res:
                final.append([arr[i],arr[i+1]])
        return final        