class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if nums == [] or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == target and nums[right] == target:
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left + 1, right - 1]

            elif nums[left] == target:
                while right - left > 0 and nums[right] > target:
                    right = (left + right) / 2

            elif nums[right] == target:
                while right - left > 0 and nums[left] < target:
                    left = (left + right) / 2 + 1

            elif right - left == 1:
                return [-1, -1]

            else:
                middle = (left + right) / 2
                if nums[middle] == target:
                    left = middle
                    right = middle
                elif nums[middle] > target:
                    right = middle
                else:
                    left = middle

        if nums[left] == target:
            return [left, left]
        else:
            return [-1, -1]




if __name__ == '__main__':
    assert Solution().searchRange([], 0) == [-1, -1]
    assert Solution().searchRange([1], 0) == [-1, -1]
    assert Solution().searchRange([1], 1) == [0, 0]
    assert Solution().searchRange([1, 4], 4) == [1, 1]
    assert Solution().searchRange([1, 5], 4) == [-1, -1]
    assert Solution().searchRange([1, 4], 1) == [0, 0]
    assert Solution().searchRange([1, 2, 2], 2) == [1, 2]
    assert Solution().searchRange([0, 0, 1, 1, 1, 4, 5, 5], 2) == [-1, -1]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([3, 3, 3, 3, 3, 3, 3], 3) == [0, 6]
    assert Solution().searchRange([2, 3, 3, 3, 3, 3, 4], 8) == [-1, -1]
