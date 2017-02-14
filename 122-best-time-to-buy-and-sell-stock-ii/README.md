Best Time to Buy and Sell Stock II
========

Description
--------

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).



Solution
--------

#### 想法

*   只要有從高變低，就有賣出重買的必要，例如`[1, 3, 2, 4]`，比較好是`[1, 3]` 和 `[2, 4]`，而不是`[1, 4]`
*   在未買進的狀態下，如果變大，那就該在前一個時間點買進。
*   在已買進的狀態下，如果變小，那就該在前一個時間點賣出。
*   最後如果在持有的狀態下結束，則該在最後一個時間點賣出。

```python
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
```

#### 參考

Basically, if tomorrow's price is higher than today's, we buy it today and sell tomorrow. Otherwise, we don't. Here is the code:

```python
class Solution(object):
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
```
