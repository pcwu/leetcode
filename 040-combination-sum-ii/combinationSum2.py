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


if __name__ == '__main__':
    assert Solution().combinationSum2([2, 3], 7)  == []
    assert Solution().combinationSum2([2, 3, 5], 7) == [[2, 5]]
    assert Solution().combinationSum2([2, 2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert Solution().combinationSum2([3, 1, 3, 5, 1, 1], 8) == \
        [[1, 1, 1, 5], [1, 1, 3, 3], [3, 5]]
    assert Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == \
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
