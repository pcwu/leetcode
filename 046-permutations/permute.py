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


if __name__ == '__main__':
    print Solution().permute([1, 2, 3, 4])
