Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.

The solution set must not contain duplicate combinations.

For example, given candidate set `[10, 1, 2, 7, 6, 1, 5]` and target `8`,
A solution set is:

```
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```


Solution
--------

*   這題跟 039 的差別就是不能重覆使用元素，但元素可能會重覆。
*   更動就是當要 recursive 子問題時，如果發現這個元素跟前一個元素相同，就跳過。
*   子問題展開的區間也要從原本的 `i` 變成 `i + 1` (因為不能重覆使用自己)

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
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
                if not (i > start and candidates[i] == candidates[i-1]):
                    findCombination(i + 1, target - candidates[i], result + [candidates[i]], results)

        candidates.sort()
        findCombination(0, target, [], results)
        return results
```
