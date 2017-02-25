Merge Intervals
========

Description
--------

Given a collection of intervals, merge all overlapping intervals.

For example,
Given `[1,3],[2,6],[8,10],[15,18]`,
return `[1,6],[8,10],[15,18]`.


Solution
--------

1.  先把所有的 Interval 依 start 排列
2.  如果前一個的尾巴跟後面一個的開頭重疊的話，合併變成 [前開頭, max(前尾巴, 後尾巴)]
3.  沒重疊就把剛剛結果存下來

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
        result = []
        intervals.sort(key=lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end

        for i in intervals:
            if end >= i.start:
                end = max(i.end, end)
            else:
                result.append([start, end])
                start, end = i.start, i.end

        result.append([start, end])
        return result
```
