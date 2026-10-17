class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        newn,c=num,0
        while newn>0:
            n=newn%10
            if num%n==0:
                c+=1
            newn//=10
        return c