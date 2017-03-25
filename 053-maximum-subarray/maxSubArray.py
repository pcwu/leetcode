class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        current = 0
        result = nums[0]

        for i in nums:
            current += i
            result = max(current, result)
            current = max(0, current)

        return result

if __name__ == '__main__':
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([-1]) == -1
