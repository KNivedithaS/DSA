class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        L = len(nums)
        if L % 2 != 0: return float(nums[L//2])
        else: return float(nums[L//2] + nums[L//2 - 1]) / 2    