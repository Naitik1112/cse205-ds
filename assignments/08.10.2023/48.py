class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        Result = []

        for i in range (len(matrix[0])):
            Result.append([])
            for j in range (len(matrix)):
                Result[i].append(matrix[len(matrix)-1-j][i])
        for i in range(len(matrix)):
            matrix.pop()
        for subsets in Result:
            matrix.append(subsets)            