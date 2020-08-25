# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Time complexity: O(N)
    # Space complexity: O(1)
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre
