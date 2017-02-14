# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


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
