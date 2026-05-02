class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        array = [0 for _ in range(n)]
        array[0] = 1
        array[1] = 2
        for i in range(2,n):
            array[i] = array[i-1]+array[i-2]
        return array[n-1]

        