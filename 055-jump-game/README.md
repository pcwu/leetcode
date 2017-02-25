Jump Game
========

Description
--------

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
`A = [2,3,1,1,4]`, return `true`.

`A = [3,2,1,0,4]`, return `false`.



Solution
--------

*   有一個指針指著目前可以跳到最遠的地方 (一開始指著start)
*   在指針的範圍內需有其中一個位置可以將指針往前推進
*   一旦推進超過尾巴(也就是有某點可以跳超過尾巴了)，回傳 `True`
*   如果走到指針還無法往前推進，就表示最遠就到這邊而已了，回傳 `False`


```python
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
```
