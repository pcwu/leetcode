Container With Most Water
========

## Python

O(n^2)暴力展開，不意外TLE

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(len(height)):
            for j in xrange(len(height)):
                if min(height[i], height[j]) * abs(i - j) > result:
                    result = min(height[i], height[j]) * abs(i - j)

        return result
```

只好改成這樣, 想法：

https://discuss.leetcode.com/topic/35117/share-my-short-java-code-with-%E4%B8%AD%E6%96%87-explanation/2

證明在這：

https://discuss.leetcode.com/topic/503/anyone-who-has-a-o-n-algorithm/2

還沒看完

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        result = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
            result = max(result, min(height[left], height[right]) * (right - left))

        return result
```
