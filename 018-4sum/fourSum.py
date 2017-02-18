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

if __name__ == '__main__':
    assert Solution().fourSum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]]
    assert Solution().fourSum([-1, 0, 1, 2, -1, -4], -1) == \
        [[-4, 0, 1, 2], [-1, -1, 0, 1]]
    assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == \
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0) == \
        [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2],
        [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
