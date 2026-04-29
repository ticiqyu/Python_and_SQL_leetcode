class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        answer = ''
        for i in range(len(s)):
            if s[i] not in answer: #новый char
                answer += s[i]
                if max_length < len(answer):
                    max_length = len(answer)
            else:
                if s[i] == answer[0]: #если самый первый char = новому
                    answer = answer.replace(s[i],"")
                    answer += s[i]
                else:
                    if max_length < len(answer):
                        max_length = len(answer)
                    idx = answer.index(s[i])
                    answer = answer[idx+1:]
                    answer += s[i]
        return max_length
                