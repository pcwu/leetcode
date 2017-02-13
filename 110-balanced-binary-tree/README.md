Balanced Binary Tree
========

Description
--------

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Code
--------


覺得題目怪怪的，`[1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5]` 明明最大深度差是 2 但答案居然是 True

本來的做法，是遍歷後，紀錄最大和最小深度差：

```python
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = {}

        def treeTraversal(node, depth):
            if not node:
                if 'min' not in result.keys() or depth < result['min']:
                    result['min'] = depth
                if 'max' not in result.keys() or depth > result['max']:
                    result['max'] = depth
            else:
                treeTraversal(node.left, depth + 1)
                treeTraversal(node.right, depth + 1)

        treeTraversal(root, 0)
        return result['max'] - result['min'] <= 1
```

後來看了別人的[討論](https://discuss.leetcode.com/topic/276/two-different-definitions-of-balanced-binary-tree-result-in-two-different-judgments?show=63)

才發現 `weight balanced tree` 和 `height balanced tree` 不一樣，所以本題只要看左右子樹的最深是否差超過1即可。

```python
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def treeTraversal(node):
            if not node:
                return 0

            leftDepth = treeTraversal(node.left)
            if leftDepth == -1:
                return -1
            rightDepth = treeTraversal(node.right)
            if rightDepth == -1:
                return -1

            if abs(leftDepth - rightDepth) > 1:
                return -1

            return max(leftDepth, rightDepth) + 1

        return treeTraversal(root) != -1
```
