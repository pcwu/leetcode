class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(price - minPrice, maxProfit)

        return maxProfit


if __name__ == "__main__":
    assert Solution().maxProfit([]) == 0
    assert Solution().maxProfit([7]) == 0
    assert Solution().maxProfit([7, 6, 5, 4]) == 0
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
