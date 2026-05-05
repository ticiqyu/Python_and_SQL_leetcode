class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        last = {int(d): i for i, d in enumerate(s)}
        
        for i, digit in enumerate(s):
            for d in range(9, int(digit), -1):
                if d in last and last[d] > i:
                    s[i], s[last[d]] = s[last[d]], s[i]
                    return int(''.join(s))
                    
        return num