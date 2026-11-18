class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x,y=0,0
        for i in nums:
            if i>9:
                x+=i
            else:
                y+=i
        if x>y or y>x:
            return True
        else:
            return False