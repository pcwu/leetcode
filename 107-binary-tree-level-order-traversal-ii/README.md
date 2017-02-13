Binary Tree Level Order Traversal II
========


Description
--------

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree `[3,9,20,null,null,15,7]`

```
3
/ \
9  20
/  \
15   7
```
return its bottom-up level order traversal as:
```
[
  [15,7],
  [9,20],
  [3]
]
```

Code
--------

```python
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        if not root:
            return []

        def treeTraversal(node, depth):
            if len(result) < depth + 1:
                new = []
                result.append(new)

            result[depth].append(node.val)

            if node.left:
                treeTraversal(node.left, depth + 1)
            if node.right:
                treeTraversal(node.right, depth + 1)

        treeTraversal(root, 0)
        result.reverse()
        return result

```
