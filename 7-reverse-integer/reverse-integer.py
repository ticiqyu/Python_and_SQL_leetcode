class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT32 = -2**31 
        MAX_INT32 = 2**31 -1
        print(type(x))
        k = 0
        flag,x = (1,x) if x>0 else (0,-x)
        while x>0:
            k = 10*k + x%10
            x = x//10
        if k <MIN_INT32 or k > MAX_INT32:
            return 0
        return k if flag else -k