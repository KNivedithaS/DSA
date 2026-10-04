class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        max_sum = nums[0]
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
                
        return max_sum
