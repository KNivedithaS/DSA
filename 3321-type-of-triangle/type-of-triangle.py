class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a=nums[0]
        b=nums[1]
        c=nums[2]
        if a+b>c and a+c>b and c+b>a:
            if a==b==c:
                return "equilateral"
            elif a==b!=c or a==c!=b or c==b!=a:
                return "isosceles"
            else:
                return "scalene"
        return "none"
            