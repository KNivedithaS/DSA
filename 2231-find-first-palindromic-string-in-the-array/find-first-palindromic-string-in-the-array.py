class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ans=""
        for i in words:
            str=i[::-1]
            if(str==i):
                ans=i
                break
        return ans
        