class Solution(object):
    def removeDuplicates(self, nums):
        st = sorted(list(set(nums)))
        nums[:len(st)] = st
        return len(st)
