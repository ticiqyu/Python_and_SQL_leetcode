class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        array = []
        if n==1:
            return True
        while n>0:
            array.append(n % 2)
            n = n//2
        return sum(array)==1
        