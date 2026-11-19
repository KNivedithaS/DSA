class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=[]
        st=sorted(nums)
        for i in range(0,len(st),2):
            c.append(st[i+1])
            c.append(st[i])
        return c