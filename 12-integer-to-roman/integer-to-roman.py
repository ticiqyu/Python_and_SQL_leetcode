class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        dividers = [1000,500,100,50,10,5,1]
        letters = ['M','D','C','L','X','V','I']
        digits = []
        for divider in dividers:
            digits.append(num//divider)
            num = num % divider
        print(digits)
        res += digits[0]*'M'
        for i in range(1,4):
            if digits[2*i] == 4:
                if digits[2*i-1]==1:
                    res+=letters[2*i] + letters[2*i-2]
                else:
                    res+=letters[2*i] + letters[2*i-1]
            else:
                res+= letters[2*i-1]*digits[2*i-1] + letters[2*i]*digits[2*i]
        return res
        
        
        



