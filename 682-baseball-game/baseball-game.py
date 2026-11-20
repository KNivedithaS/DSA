class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        c=[]
        for x in operations:
            if x=='C':
                c.pop()
            elif x=='D':
                c.append(2*c[-1])
            elif x=='+':
                c.append(c[-1]+c[-2])
            else:
                c.append(int(x))
        return sum(c)