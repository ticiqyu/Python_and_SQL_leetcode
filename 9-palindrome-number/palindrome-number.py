class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        l = []
        while x > 0:
            l.append(x%10)
            x = x//10
        return l==l[::-1]


            
                
