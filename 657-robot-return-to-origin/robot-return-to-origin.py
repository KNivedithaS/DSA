class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c,c1=0,0
        for x in moves:
            if x=='U':
                c+=1
            elif x=='D':
                c-=1
            elif x=='L':
                c1+=1
            else:
                c1-=1
        if c==0 and c1==0:
            return True
        return False