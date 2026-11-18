class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1=0
        for x in nums:
            if x<10:
                sum1+=x
            else:
                sum1-=x
        if sum1!=0:
            return True
        return False