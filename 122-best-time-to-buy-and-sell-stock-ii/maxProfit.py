class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        lastPrice = prices[0]
        buyPrice = prices[0]
        sumProfit = 0
        isHold = False

        for price in prices[1:]:
            if isHold is False and price > lastPrice:
                buyPrice = lastPrice
                isHold = True
            elif isHold is True and price < lastPrice:
                sumProfit += lastPrice - buyPrice
                isHold = False
            lastPrice = price

        if isHold:
            sumProfit += lastPrice - buyPrice

        return sumProfit


if __name__ == "__main__":
    assert Solution().maxProfit([]) == 0
    assert Solution().maxProfit([7]) == 0
    assert Solution().maxProfit([2, 1]) == 0
    assert Solution().maxProfit([1, 2]) == 1
    assert Solution().maxProfit([7, 6, 5, 4]) == 0
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
