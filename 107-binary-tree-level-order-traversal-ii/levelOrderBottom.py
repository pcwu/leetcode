# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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
