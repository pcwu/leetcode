Generate Parentheses
========

Description
--------

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

Solution
--------

*   用一個 `result` 來儲存結果，一但有出現一個新的結果，就 `append` 進去。
*   `generate` 的四個輸入分別是 還有幾個左刮號、右刮號可以用，疊到目前為止的狀態，result 的 ref
*   2種狀況下會展開：
    *   一個是還有左刮號可以用時，就插入左刮號，然後 recursive 子問題
    *   一個是能用的左刮號比右刮號多時，表示現在也可以插入右刮號，一樣 recursive 子問題


```python
class Solution(object):
    def generate(self, left, right, str, result):
        if left == 0 and right == 0:
            result.append(str)
            return
        if left > 0:
            self.generate(left - 1, right, str + "(", result)
        if right > left:
            self.generate(left, right - 1, str + ")", result)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate(n, n, "", result)
        return result
```
