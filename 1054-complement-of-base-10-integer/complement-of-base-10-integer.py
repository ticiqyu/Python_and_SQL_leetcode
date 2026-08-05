class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 0
        a = 1
        while a < n:
            a*=2
        if a == n:
            return a-1
        return a - 1 -n