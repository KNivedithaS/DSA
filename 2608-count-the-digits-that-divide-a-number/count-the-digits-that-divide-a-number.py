class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = num
        ans = 0
        while x>0:
            dig = x%10
            if num%dig == 0:
                ans += 1
            x = x//10
        return ans