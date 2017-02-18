4 Sum

Description
--------

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.


```
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

Solution
--------


建立 hash table 然後正常做會超時: `O(n^3)`

(是說不超時就不要算中級了)

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []

        nums.sort()
        result = set()
        numsIndex = {}

        for i in xrange(len(nums)):
            if nums[i] in numsIndex.keys():
                numsIndex[nums[i]].append(i)
            else:
                numsIndex[nums[i]] = [i]

        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                subTarget = target - nums[i] - nums[j]
                for k in xrange(j + 1, len(nums)):
                    if subTarget - nums[k] in numsIndex.keys():
                        for l in numsIndex[subTarget - nums[k]]:
                            if l > k:
                                result.add((nums[i], nums[j], nums[k], nums[l]))

        return sorted([list(t) for t in result])
```

看到別人強大清爽的解法，適用於任何值的 N-Sum：

*   當 `N == 2` 時，就是簡單的 2-Sum 解法
*   當 `N > 2` 時，取一個值並化為 `N-1` 的子問題
*   注意一開頭可以刪掉一些不可能的狀況 `target < nums[0] * n or target > nums[-1] * n`


```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNSum(nums, target, n, result, results):
            if len(nums) < n or target < nums[0] * n or target > nums[-1] * n:
                return

            if n == 2:
                l = 0
                r = len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            else:
                for i in xrange(len(nums) - n + 1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNSum(nums[i + 1:], target - nums[i], n-1, result + [nums[i]], results)

        results = []
        findNSum(sorted(nums), target, 4, [], results)
        return results
```
