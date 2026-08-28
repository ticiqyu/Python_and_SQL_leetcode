class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        max_ans = ''
        ans = ''
        for i in range(len(s)):
            ans = s[i] #текущий символ
            j = i+1 #начинаем со следующей позиции?
            while j<=len(s)-1:
                ans += s[j]
                if ans == ans[::-1] and len(ans)>=len(max_ans):
                    max_ans = ans
                j+=1
            
        return ans if ans == ans[::-1] and len(ans)>=len(max_ans) else max_ans


            
        