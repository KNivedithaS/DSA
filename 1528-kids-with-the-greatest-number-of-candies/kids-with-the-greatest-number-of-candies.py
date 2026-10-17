class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ans=[]
        x=sorted(candies)
        high=x[len(x)-1]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=high:
                res=True
            else:
                res=False
            ans.append(res)
        return ans