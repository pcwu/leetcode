# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

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


if __name__ == '__main__':
    print Solution().merge([])
    print Solution().merge([Interval(1, 4), Interval(2, 5)])
    print Solution().merge([Interval(1, 4), Interval(2, 3)])
    print Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)])
    # [1,6],[8,10],[15,18]
