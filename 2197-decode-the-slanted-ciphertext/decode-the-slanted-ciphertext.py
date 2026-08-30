class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        n = len(encodedText)//rows
        s = ''
        for i in range(n):
            k = 0
            while i + k * (n + 1) < len(encodedText):
                s += encodedText[i + k * (n + 1)]
                k+=1
        return s.rstrip()

        