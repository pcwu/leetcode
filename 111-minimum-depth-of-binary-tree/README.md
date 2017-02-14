Minimum Depth of Binary Tree
========


Description
--------

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.



Solution
--------

想法是用一個 `min` 來紀錄最小深度的 leaf，如果搜尋時已經等於最小深度，就可以提早離開不用繼續了。

Leaf 的定義是左子樹和右子樹都是 `None`


```python
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        result = {}

        def treeTraversal(node, depth):
            if 'min' in result.keys() and depth >= result['min']:
                return -1

            if node.left is None and node.right is None:
                if 'min' not in result.keys() or depth < result['min']:
                    result['min'] = depth
                return -1

            if node.left:
                treeTraversal(node.left, depth + 1)
            if node.right:
                treeTraversal(node.right, depth + 1)

        treeTraversal(root, 1)
        return result['min']
```

以下是神手的解法：

```python
def minDepth(self, root):
    if not root: return 0
    d = map(self.minDepth, (root.left, root.right))
    return 1 + (min(d) or max(d))

def minDepth(self, root):
    if not root: return 0
    d, D = sorted(map(self.minDepth, (root.left, root.right)))
    return 1 + (d or D)
```
