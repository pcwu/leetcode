026. Remove Duplicates from Sorted Array
========

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Code
--------

直接用List.remove()移除元件是不可行的，因為他驗證的方式，還是會看到原本的值

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = None
        result = 0

        for i in nums:
            if i != pre:
                pre = i
                result += 1
            else:
                nums.remove(i)

        return result
```

所以刪除後要將後面的值往前搬，變成這樣：

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = None
        result = 0
        tail = 0

        for i in xrange(len(nums)):
            if nums[i] != pre:
                pre = nums[i]
                nums[tail] = nums[i]
                result += 1
                tail += 1

        return result
```
