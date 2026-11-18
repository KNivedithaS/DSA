class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max=1
        for x in sentences:
            st=x
            if max<len(x.split()):
                max=len(x.split())
        return max