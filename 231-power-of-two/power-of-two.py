class Solution(object):
    def isPowerOfTwo(self, n):
        if n==1:
            return True
        if n==2:
            return True
        if n > 2:
            if n % 2 == 0:
                ans= n // 2
                return self.isPowerOfTwo(ans)
        return False
        