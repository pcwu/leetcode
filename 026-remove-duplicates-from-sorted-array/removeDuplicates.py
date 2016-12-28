class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = None
        result = 0
        tail = 0

        for i in xrange(len(nums)):
            if num[i] != pre:
                pre = num[i]
                nums[tail] = nums[i]
                result += 1
                tail += 1

        return result
