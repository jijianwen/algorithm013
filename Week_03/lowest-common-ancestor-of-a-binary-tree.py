# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(curr):
            if not curr: return False

            l = dfs(curr.left)
            r = dfs(curr.right)

            if (l is True and r is True) or ((curr.val == p.val or curr.val == q.val) and (l is True or r is True)):
                self._comm = curr

            if l is True or r is True or (curr.val == p.val or curr.val == q.val):
                return True

        dfs(root)
        return self._comm
"""
node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(6)
node5 = TreeNode(2)
node6 = TreeNode(0)
node7 = TreeNode(8)
node8 = TreeNode(7)
node9 = TreeNode(4)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node7
node3.right = node8

node5.left = node8
node5.right= node9

obj = Solution()
common = obj.lowestCommonAncestor(node1, node2, node3)
print("lowest common ancestor:{}".format(common.val))
"""
