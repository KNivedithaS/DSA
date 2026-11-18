class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum1,sum2=1,1
        for x in nums:
            if x<10:
                sum1+=x
            else:
                sum2+=x
        if sum1!=sum2:
            return True
        return False