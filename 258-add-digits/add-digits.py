class Solution:
    def addDigits(self, num: int) -> int:
        d = 0
        while d+num>9:
            d+= num%10
            num = num//10
            if num == 0:
                num,d = d,num
        return d+num
        