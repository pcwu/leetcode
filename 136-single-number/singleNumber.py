class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0
        for i in nums:
            result ^= i
        return result


if __name__ == "__main__":
    assert Solution().singleNumber([1]) == 1
    assert Solution().singleNumber([1, 2, 3, 4, 3, 2, 1]) == 4
