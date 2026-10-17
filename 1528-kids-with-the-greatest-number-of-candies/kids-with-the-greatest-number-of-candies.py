class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans=[]
        high=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=high:
                res=True
            else:
                res=False
            ans.append(res)
        return ans