class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m=0
        for i in accounts:
            sum=0
            for j in i:
                sum+=j
            m=max(sum,m)
        return m