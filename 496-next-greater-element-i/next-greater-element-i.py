class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            if num == max(nums2):
                ans.append(-1)
            else:
                i = nums2.index(num)
                while nums2[i] <= num:
                    i += 1
                    if i == len(nums2):
                        ans.append(-1)
                        break
                    if nums2[i] > num:
                        ans.append(nums2[i])
                        break
        return ans