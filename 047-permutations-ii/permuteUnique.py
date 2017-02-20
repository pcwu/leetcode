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


if __name__ == '__main__':
    assert Solution().permuteUnique([1, 1, 1]) == [[1, 1, 1]]
    assert Solution().permuteUnique([1, 1, 3, 4]) == \
        [[1, 1, 3, 4], [1, 1, 4, 3], [1, 3, 1, 4], [1, 3, 4, 1],
        [1, 4, 1, 3], [1, 4, 3, 1], [3, 1, 1, 4], [3, 1, 4, 1],
        [3, 4, 1, 1], [4, 1, 1, 3], [4, 1, 3, 1], [4, 3, 1, 1]]
