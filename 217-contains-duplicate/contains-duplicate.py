class Solution(object):
    def containsDuplicate(self, nums):
        st=set(nums)
        if len(st)!=len(nums):
            return True
        return False