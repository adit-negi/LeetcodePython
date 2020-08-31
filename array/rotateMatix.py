class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        numrows = len(matrix)
        Mat = [[0 for i in range(numrows)] for j in range(numrows)]
        for i in range(numrows):
            for j in range(numrows):
                Mat[j][numrows-1-i] = matrix[i][j]
        for i in range(numrows):
            for j in range(numrows):
                matrix[i][j] = Mat[i][j]
