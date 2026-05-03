class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        array = []
        while n>0:
            array.append(n%3)
            n = n//3
        return sum(array)==1
        