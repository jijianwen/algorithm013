# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Time complexity:  O(NlogN)
    # Space complexity: O(logN)
    def findMid(self, left, right):
        slow = fast = left
        while fast != right and fast.next != right:
            slow = slow.next
            fast = fast.next.next
        return slow

    def buildBST(self, left, right):
        if (left == right):
            return None

        mid = self.findMid(left, right)
        node = TreeNode(mid.val)
        node.left = self.buildBST(left, mid)
        node.right = self.buildBST(mid.next, right)

        return node

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.buildBST(head, None)

