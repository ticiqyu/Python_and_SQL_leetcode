class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        n = len(words)
        candidates = []
        for i in range(n):
            if words[i] == target:
                candidates.append(i)
        print(candidates)
        return min([min(i+startIndex,(n-i+startIndex)%n,(n+i-startIndex)%n) for i in candidates])
        