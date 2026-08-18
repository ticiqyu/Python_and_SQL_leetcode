class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        for i in range(len(mat)):
            for j in range(n):
                if i % 2:
                    if mat[i][(j+k)%n] != mat[i][j]:
                        return False
                else:
                    if mat[i][(j-k)%n] != mat[i][j]:
                        return False
        return True

        