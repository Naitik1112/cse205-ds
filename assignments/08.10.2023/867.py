class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        Result = []
        for i in range(0,len(matrix[0])):
            Result.append([])
            for j in range(0,len(matrix)):
                Result[i].append(matrix[j][i])
        return Result        