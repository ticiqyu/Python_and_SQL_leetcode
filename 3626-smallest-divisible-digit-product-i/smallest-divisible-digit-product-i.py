class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            n_iter = n
            prod = 1
            while n_iter > 0:
                prod = prod * (n_iter % 10)
                n_iter = n_iter // 10
            if prod % t == 0:
                return n
            n += 1