class Solution:
    def isHappy(self, n: int) -> bool:
        array = []
        while (1):
            sum = 0
            while n > 0: # сумма квадратов числа
                sum += (n % 10)**2
                n = n//10
            
            if sum == 1:
                return True
            else:
                if sum not in array:
                    array.append(sum)
                    n = sum
                else:
                    return False
            
        