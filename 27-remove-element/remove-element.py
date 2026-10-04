class Solution(object):
    def removeElement(self, nums, val):
        n=len(nums)
        lt=0
        for i in range(n):
            if nums[i]!=val:
                nums[lt]=nums[i]
                lt+=1
        return lt