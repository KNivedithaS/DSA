class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            str=i[::-1]
            if str==i:
                return i
        return ''
        