class Solution(object):
    def signFunc(self,x):
        if x==0:
            return 0
        elif x>0:
            return 1
        return -1 
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=1
        for x in nums:
            p*=x
        return self.signFunc(p)