class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while r > l:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                elif abs(target - s) < abs(target - result):
                    result = s

                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
        return result

if __name__ == "__main__":
    assert Solution().threeSumClosest([0, 0, 0], 1) == 0
