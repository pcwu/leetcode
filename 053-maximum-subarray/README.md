Description
--------

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`,
the contiguous subarray `[4,-1,2,1]` has the largest `sum = 6`.


Solution
--------

*   想法很簡單，就是一路往下走，一路邊紀錄最大值
*   如果到目前為止是負的，就表示沒有幫助，不需要了，重新開始
*   記得一開始 result 要設定成 `nums[0]` 而不是 `0`，不然只有負數的 input 會錯誤


```python
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
    assert Solution().permuteUnique([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().permuteUnique([-1]) == -1

```
