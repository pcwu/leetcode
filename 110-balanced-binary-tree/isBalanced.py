# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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
