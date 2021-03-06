# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Time complexity: O(N)
    # Space complexity: O(1)
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        pre = dummy

        while head and head.next:
            first = head
            second = head.next

            pre.next = second
            first.next = second.next
            second.next = first

            pre = first
            head = first.next

        return dummy.next

    # Recursion
    # Time complexity:  O(N)
    # Space complexity: O(N)
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head
