class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == '':
            return 0
        sign = 1
        res = ''
        i = 0
        while i+1<len(s) and (s[i]=='-' or s[i] == '+'):
            if s[i+1] == '-' or s[i+1] == '+':
                return 0
            sign = -1 if s[i] == '-' else 1
            i+=1

        while s[i].isdigit():
            res += s[i]
            i+=1
            if i == len(s):
                break
        res = '0' if res=='' else res
        if sign*int(res)> 2**31 -1: 
            return  2**31 -1
        elif sign*int(res) < -2**31:
            return -2**31
        else:
            return sign*int(res) 
