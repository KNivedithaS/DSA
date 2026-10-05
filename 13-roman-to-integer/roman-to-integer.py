class Solution(object):
    def romanToInt(self, s):
        romanchar=['M', 'D', 'C', 'L', 'X', 'V', 'I']
        charval=[1000,500,100,50,10,5,1]
        n,sum=len(s),0
        for i in range(n):
            value,nextvalue=0,0
            for j in range(7):
                if s[i]==romanchar[j]:
                    value=charval[j]
                    break
            if i+1<n:
                for j in range(7):
                    if s[i+1]==romanchar[j]:
                        nextvalue=charval[j]
                        break
            if value<nextvalue:
                sum-=value
            else:
                sum+=value
        return sum