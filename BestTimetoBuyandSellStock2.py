class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        for i in range(1, len(prices)):
            # If the current price is greater than the previous day's price,
            # we can make a profit by buying on the previous day and selling on the current day.
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit
