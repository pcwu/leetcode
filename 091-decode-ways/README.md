Description
--------

A message containing letters from A-Z is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.


Solution
--------


*   最麻煩需要處理的就是 `0`，所以從尾巴往前做是比較理想的
*   先把整個 DP 的紀錄填零(並額外新增一位數)，並先處理最後2位數
*   再來就是從後面往前做，如果是零的話就跳過
*   如果後面2位加起來小於26的話，表示可以2種延伸，所以是 `dp[i] = dp[i + 1] + dp[i + 2]`
*   如果是大於 26 的話 `dp[i] = dp[i + 1]`

```python
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)]
        dp[len(s)] = 1
        dp[len(s) - 1] = 1 if s[len(s) - 1] != '0' else 0

        for i in range(len(s) - 2, -1, -1):
            if s[i] != '0':
                if int(s[i:i + 2]) <= 26:
                    dp[i] = dp[i + 1] + dp[i + 2]
                else:
                    dp[i] = dp[i + 1]

        return dp[0]
```
