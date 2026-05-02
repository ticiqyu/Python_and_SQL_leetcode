class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while (1):
            if x>=i*i:
                i+=1
            else:
                return i-1