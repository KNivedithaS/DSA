class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        c=[]
        for i in range(len(words)):
            if x in words[i]:
                c.append(i)
        return c