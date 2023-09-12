class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        sell = prices[0]

        profit = sell - buy

        for price in prices:
            if (buy > price):
                buy = price
                sell = price
            elif (sell < price):
                sell = price
            if sell-buy > profit:
                profit = sell - buy
        return profit
