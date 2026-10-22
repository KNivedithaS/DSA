class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch=0
        for char in s.strip()[::-1]:
            if char!=" ":
                ch+=1
            else:
                break
        return ch