class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = 1
        while n>=i:
            if digits[n-i]<9: # последняя цифра не 9
                digits[n-i]+=1
                return digits
            else: # последняя цифра 9
                digits[n-i] = 0 
                if n-i-1<0: #если последняя цифра - первая
                    digits.insert(0,1)
                    return digits
                elif digits[n-i-1]==9: #если перед последней цифры 9
                    i+=1
                else: #если перед последней цифрой не 9
                    digits[n-i-1]+=1
                    return digits
                    

        