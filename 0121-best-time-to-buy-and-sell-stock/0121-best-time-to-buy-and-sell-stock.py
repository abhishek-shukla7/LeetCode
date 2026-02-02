class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n=len(prices)
        min_profit=float("inf")
        max_profit=0

        for i in range(0,n):
            min_profit=min(min_profit,prices[i])
            max_profit=max(max_profit,prices[i]-min_profit)

        return max_profit