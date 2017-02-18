Search for a Range
========

Description
--------

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return `[-1, -1]`.

For example,
Given `[5, 7, 7, 8, 8, 10]` and target value 8,
return `[3, 4]`.


Solution
--------

這題解得很難看，又沒有真的 `O(logn)`

*   一開始就要跳出的狀況： `target < left` 或 `target > right` 或 `nums =[]`
*   接下來目標就是對半對半切，盡快讓 `left` 和 `right` 抓到 `target`
*   一但兩邊都抓到，就盡快往左跟右探到底，再輸出。
*   `left` 和 `right` 相當接近時，會有問題，所以為了修這些問題整個程式面目全非。

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if nums == [] or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == target and nums[right] == target:
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left + 1, right - 1]

            elif nums[left] == target:
                while right - left > 0 and nums[right] > target:
                    right = (left + right) / 2

            elif nums[right] == target:
                while right - left > 0 and nums[left] < target:
                    left = (left + right) / 2 + 1

            elif right - left == 1:
                return [-1, -1]

            else:
                middle = (left + right) / 2
                if nums[middle] == target:
                    left = middle
                    right = middle
                elif nums[middle] > target:
                    right = middle
                else:
                    left = middle

        if nums[left] == target:
            return [left, left]
        else:
            return [-1, -1]
```


別人精簡的解法：
