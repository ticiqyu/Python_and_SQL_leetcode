class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] != 0 and i>0:
                    matrix[i][j] += matrix[i-1][j]
            currRow = sorted(matrix[i], reverse = True)
            for k in range(len(currRow)):
                ans =  currRow[k] * (k+1) if ans < currRow[k] * (k+1) else ans
        return ans

        