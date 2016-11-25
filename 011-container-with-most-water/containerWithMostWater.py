#!/usr/lib/python


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

print Solution().maxArea([30, 3, 10, 6, 7, 5])
