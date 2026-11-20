class Solution(object):
    def differenceOfSum(self, nums):
        element_sum=sum(nums)
        for i in nums:
            while i > 0:
                element_sum -= i%10
                i=i//10
        return element_sum
