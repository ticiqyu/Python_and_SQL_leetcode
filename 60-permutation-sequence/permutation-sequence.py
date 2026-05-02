class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        char = ''
        ans = ''
        count = n
        word = [str(i+1) for i in range(count)]
        k = k-1
        for i in range(count):
            factor = factorial(n-1)
            whole_part = k//factor 
            char = word[whole_part]
            k %= factor
            ans += char
            word.remove(char)
            n-=1
        return ans

    def factorial(n:int)->int:
        return n*factorial(n-1) if n > 1 else 1


        