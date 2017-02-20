Permutations
========

Description
--------

Given a collection of distinct numbers, return all possible permutations.

For example,
`[1,2,3]` have the following permutations:

```
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

Solution
--------

*   每個元素輪流當第一，然後就變成子問題了

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permuteIt(nums, current, results):
            for i in range(len(nums)):
                if len(nums) == 1:
                    results.append(current + nums)
                else:
                    permuteIt(nums[:i] + nums[i + 1:], current + [nums[i]], results)

        results = []
        permuteIt(sorted(nums), [], results)
        return results

```
