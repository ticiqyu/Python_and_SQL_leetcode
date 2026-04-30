class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[0::]==str(x)[::-1]