001.Two Sum
========

Problem Description
--------

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.



Code
--------

這樣寫最直觀，但只比22%的人快。時間複雜度為O(n^2)，額外的空間需求為O(1)。
把2個range改成xrange後反而變慢了，原因不明。

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

網路上看到有人的做法是，先用一個hash table來存，key記錄差多少會為target，value紀錄index值。所以每個數都去查詢是否有自己這個值的key就行了。

```python
class Solution(object):
    def twoSum(self, nums, target):
        buff_dict = {}
        for i in xrange(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
```
