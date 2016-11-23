#!/usr/lib/python


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

print Solution().maxArea([3, 3, 10, 6, 7, 5])
