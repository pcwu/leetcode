Best Time to Buy and Sell Stock
========

Description
--------

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.


```
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
```


```
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
```


Code
--------

```python
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

```
