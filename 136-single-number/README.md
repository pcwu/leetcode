Single number
========

Description
--------

Given an array of integers, every element appears twice except for one. Find that single one.

**Note:**

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Code
--------

*   一開始用 `dict` 來存，沒看過的數字就存進去，看過的就刪掉，最後剩下的就是答案(但超時)
*   後來才想到用 `XOR` 的方式，又快又不耗記憶體

```python
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
```
別人的解法：

```python
def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def singleNumber2(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res

def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)

def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)

def singleNumber(self, nums):
    return reduce(operator.xor, nums)
```
