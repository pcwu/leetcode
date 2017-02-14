Pascal's Triangle
========


Description
--------

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,

Return

```
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

Code
--------
```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []

        pascals = [[1]]

        for i in range(1, numRows):
            pascals.append([pascals[i - 1][0]])
            for j in range(len(pascals[i - 1]) - 1):
                pascals[i].append(pascals[i - 1][j] + pascals[i - 1][j + 1])
            pascals[i].append(pascals[i - 1][-1])
        return pascals
```
