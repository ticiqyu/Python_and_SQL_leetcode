class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        index_1,index_2 = nums.index(max(nums)),nums.index(min(nums))
        index_1,index_2 = (index_1,index_2) if index_1 < index_2 else (index_2,index_1) # ближайший индекс - index_1
        n = len(nums)
        return min(n-index_1,index_2 + 1, index_1 + 1 + (n - index_2))


