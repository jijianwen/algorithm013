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
        if root is None:
            return 0
        
        min_left = self.minDepth(root.left)
        min_right = self.minDepth(root.right)

        if min_left == 0 or min_right == 0:
            min_depth = max(min_left, min_right)
        else:
            min_depth = min(min_left, min_right)
        return 1 + min_depth
