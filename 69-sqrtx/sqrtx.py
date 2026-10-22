class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2: 
            return x
        l=x
        while l*l>x:
            l=(l+x/l)/2
        return l