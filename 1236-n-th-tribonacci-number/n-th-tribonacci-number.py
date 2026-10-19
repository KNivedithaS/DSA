class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1 :
            return n
        a=0
        b=1
        c=1
        for i in range(3,n+1):
            a,b,c=b,c,a+b+c
        return c