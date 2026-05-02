class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 or m == 1:
            return 1
        array = [1 for i in range(n-1)]
        sum = 1
        for _ in range(m-1):
            for i in range(1,n-1):
                array[i] = array[i] + array[i-1]
            sum+=array[n-2] 
        return sum