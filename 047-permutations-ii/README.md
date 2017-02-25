Permutations II
========

Description
--------

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
`[1,1,2]` have the following unique permutations:

```
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

Solution
--------

*   每個元素輪流當第一，然後就變成子問題了
*   同樣的元素，如果跟前一個一樣就不能再當頭了。

```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permuteIt(nums, current, results):
            for i in range(len(nums)):
                if len(nums) == 1:
                    results.append(current + nums)
                elif not (i > 0 and nums[i] == nums[i - 1]):
                    permuteIt(nums[:i] + nums[i + 1:], current + [nums[i]], results)

        results = []
        permuteIt(sorted(nums), [], results)
        return results

```
