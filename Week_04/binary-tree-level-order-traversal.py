# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Time complexity: O(n)
    # Space complexity: O(n)
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []

        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            res.append(level)

        return res
    # DFS
    # Time complexity: O(n)
    # Space complexity: O(n)
    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def dfs(node, level):
            if node is None: return

            if len(res) == level: res.append([])

            res[level].append(node.val)
            if node.left: dfs(node.left, level + 1)
            if node.right: dfs(node.right, level + 1)

        dfs(root, 0)

        return res

