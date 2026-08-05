class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        min_num = min(nums)
        max_num = max(nums)
        for i in range(min_num,max_num+1):
            if i not in nums:
                ans.append(i)
        return ans
        