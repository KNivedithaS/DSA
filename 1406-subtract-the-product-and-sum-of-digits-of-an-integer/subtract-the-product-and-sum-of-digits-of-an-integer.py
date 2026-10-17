class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp=n
        add=0
        pro=1
        while temp>0:
            r=temp%10
            add+=r
            pro*=r
            temp//=10
        return pro-add