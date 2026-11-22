class Solution(object):
    def maximumWealth(self, accounts):
        max=0
       
        for customer in accounts:
            sum=0
            for money in customer:
                sum=sum+money

            if sum>max:
                max=sum

        return max