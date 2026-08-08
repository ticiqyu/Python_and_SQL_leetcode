class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        for i in range(4):
            if s1[i] != s2[(i+2)%4] and s1[i] != s2[i]:
                return False
            if s2[i] != s1[(i+2)%4] and s2[i] != s1[i]:
                return False
        return True