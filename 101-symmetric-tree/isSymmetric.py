# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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
