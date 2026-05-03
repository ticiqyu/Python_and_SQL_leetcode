class Solution:
    def trailingZeroes(self, n: int) -> int:
        count_twos = 0
        count_fives = 0
        for i in range(1,n+1):
            j = i 
            while j % 2 == 0:
                count_twos+=1
                j= j//2
            while j % 5 == 0:
                count_fives += 1
                j=j//5
        return min(count_fives,count_twos)
            
        