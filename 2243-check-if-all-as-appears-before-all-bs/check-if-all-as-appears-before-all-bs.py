class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=0
        for i in range(len(s)):
            if s[i]!='a':
                c=1
            if c==1 and s[i]=='a':
                return False
        return True
