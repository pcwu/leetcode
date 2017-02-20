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


if __name__ == '__main__':
    print Solution().combinationSum([2, 3], 7) # == [[2, 2, 3]]
    print Solution().combinationSum([2, 3, 5], 7) # == [[2, 2, 3], [2, 5]]
    print Solution().combinationSum([2, 3, 6, 7], 7) # == [[2, 2, 3], [7]]
