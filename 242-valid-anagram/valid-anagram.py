class Solution(object):
    def isAnagram(self, s, t):
        sorteds= "".join(sorted(s))
        sortedt="".join(sorted(t))
        flag=0
        if len(s)==len(t):
            for i in range(len(s)):
                if sorteds[i]!=sortedt[i]:
                    flag+=1
            if flag==0:
                return True
            else:
                return False
        else:
            return False

        