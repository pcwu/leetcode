Description
--------

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![](/assets/images/README-6bac9.png)



Solution
--------

*   就只是單純的排列組合
*   如果是 `3 * 7` 的方陣，就是要走 `2 * 6`，所以是 (2+6)! / 2!6!
*   最大值可能會有100，但 `100!` 可能會溢位，所以要事先除掉

以下這個 code 打敗 100% 的人：

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        x, y = m - 1, n - 1
        if x == 0 or y == 0:
            return 1

        divide = range(2, min(x, y) + 1)
        result = 1

        for i in xrange(max(x, y) + 1, x + y + 1):
            current = i
            for j in range(len(divide)):
                if current % divide[j] == 0:
                    current = current / divide.pop(j)
                    break
            result = result * current

        for i in divide:
            result /= i

        return result
```

*   上面的方法發現要事先除掉有點麻煩，改成 DP 的方式來做
*   每個點可以到的方法數，是可以到他的上方跟左方的方法數的和
*   也就 (x, y) = (x-1, y) + (x, y-1)

```python
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        array = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                array[i][j] = array[i - 1][j] + array[i][j - 1]

        return array[m - 1][n - 1]
```
