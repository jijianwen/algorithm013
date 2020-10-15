"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None

        deque = collections.deque()
        deque.append(root)

        while deque:
            length = len(deque)

            pre = None
            for i in range(length):
                node = deque.popleft()
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
                if i > 0: pre.next = node
                pre = node

        return root
