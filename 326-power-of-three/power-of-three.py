class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        if n ==3:
            return True
        if n > 3:
            if n % 3 == 0:
                ans= n // 3
                return self.isPowerOfThree(ans)
        return False
        