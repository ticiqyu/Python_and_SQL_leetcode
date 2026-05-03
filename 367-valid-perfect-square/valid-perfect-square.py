class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i <= num/i:
            if num/i == i:
                return True
            else:
                i+=1
        return False

        