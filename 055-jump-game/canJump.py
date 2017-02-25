class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farest = 0

        for i in range(len(nums)):
            if farest >= len(nums) - 1:
                return True
            if farest < i:
                return False
            farest = max(farest, i + nums[i])

        return True




if __name__ == '__main__':
    assert Solution().canJump([]) is True  # True
    assert Solution().canJump([0]) is True  # True
    assert Solution().canJump([5]) is True  # True
    assert Solution().canJump([2, 0]) is True  # True
    assert Solution().canJump([8, 5]) is True  # True
    assert Solution().canJump([2, 5, 0, 0]) is True  # True
    assert Solution().canJump([2, 3, 1, 1, 4]) is True  # True
    assert Solution().canJump([3, 2, 1, 0, 4]) is False  # False
    assert Solution().canJump([6, 0, 0, 0, 0, 0, 1]) is True  # True
    assert Solution().canJump([6, 0, 0, 0, 0, 0, 0, 1]) is False  # False
