class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c=[]
        for i in range(len(arr)):
            if arr[i]%2!=0:
                c.append(arr[i])
            else:
                c.append(0)
        for i in range(len(c)-2):
            if c[i]!=0 and c[i+1]!=0 and c[i+2]!=0:
                return True
        return False

