class Solution:
    def lastRemaining(self, n: int) -> int: 
        first = 1 
        step = 1 
        remain = n 
        left_to_right = True 
        while remain > 1: 
            if left_to_right or remain % 2 == 1: 
                first += step 
            remain //= 2 
            step *= 2 
            left_to_right = not left_to_right 
        return first      