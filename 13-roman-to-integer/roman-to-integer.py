class Solution:
   def romanToInt(self, s: str) -> int:
        number = 0
        roman = { 'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for (current_char,next_char) in zip(s,s[1:]):
            if roman[current_char] < roman[next_char]:
                number -= roman[current_char]
            else:
                number+=roman[current_char]
        
        number+=roman[s[-1]]

        return number