class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>=0:
            revnum=0
            orgnum=x
            while x>0:
                r=x%10
                revnum=revnum*10+r
                x//=10
            if revnum==orgnum:
                return True
            else:
                return False
        else:
            return False