class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rev = 0
        for i in range(32):
            rev = (rev << 1) | (n & 1)
            n = n >> 1 
        return rev