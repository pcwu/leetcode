Symmetric Tree
========

Description
--------


Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:



Code
--------

想法是用 Recursive，左右兩顆子樹的內側和外側分別檢查是否相同，如果一有不相同就盡早回傳 `False`

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symmetric(treeLeft, treeRight):
            if treeLeft is None and treeRight is None:
                return True
            if treeLeft.val != treeRight.val:
                return False

            outter = False
            inner = False
            if treeLeft.left is None and treeRight.right is None:
                outter = True
            elif treeLeft.left is None or treeRight.right is None:
                return False
            else:
                if symmetric(treeLeft.left, treeRight.right):
                    outter = True
                else:
                    return False

            if treeLeft.right is None and treeRight.left is None:
                inner = True
            elif treeLeft.right is None or treeRight.left is None:
                return False
            else:
                if symmetric(treeLeft.right, treeRight.left):
                    inner = True
                else:
                    return False
            return inner and outter

        return symmetric(root, root)
```

後來看到別人寫得好精簡，但比起來我的可以比較早知道false 並且跳出：

```python
def isSymmetric(self, root):
    def isSym(L,R):
        if not L and not R: return True
        if L and R and L.val == R.val:
            return isSym(L.left, R.right) and isSym(L.right, R.left)
        return False
    return isSym(root, root)
```
