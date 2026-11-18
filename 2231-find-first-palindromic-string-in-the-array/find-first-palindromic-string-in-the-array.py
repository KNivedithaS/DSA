class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for x in words:
            st=x
            if x==st[::-1]:
                return st
        return '' 