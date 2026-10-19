class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        star=sorted(nums)
        ans=[]
        for i in range(len(star)):
            if star[i]==target:
                ans.append(i)
        return ans

        