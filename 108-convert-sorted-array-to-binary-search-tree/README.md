Convert Sorted Array to Binary Search Tree
========

Description
--------

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.


Code
--------

試跑了測資，發現長度為偶數時，是中間偏左邊一個為 root。於是很簡單把root找出來後，其他就變成小問題了， Recursive 結束！

```python
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) / 2 if len(nums) % 2 == 1 else len(nums) / 2 - 1

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
```
