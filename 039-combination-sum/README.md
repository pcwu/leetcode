Combination Sum
========


Description
--------

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set `[2, 3, 6, 7]` and target `7`,
A solution set is:
```
[
  [7],
  [2, 2, 3]
]
```



Solution
--------

*   先把 array 從小到大排序
*   解法為 recursive, 把 array 中每一個值都插入一次後的子問題。
*   因為可以重覆使用，所以插入值也要包含現在所在的起始值。


```python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []

        def findCombination(start, target, result, results):
            if target == 0:
                results.append(result)
            for i in range(start, len(candidates)):
                if target < candidates[i]:
                    return
                findCombination(i, target - candidates[i], result + [candidates[i]], results)

        candidates.sort()
        findCombination(0, target, [], results)
        return results
```
