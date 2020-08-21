# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        max_l = self.maxDepth(root.left)
        max_r = self.maxDepth(root.right)

        return 1 + max(max_l, max_r)
