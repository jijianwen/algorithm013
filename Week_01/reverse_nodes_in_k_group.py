# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Time complexity:  O(N)
    # Space complexity: O(1)
    def reverse(self, head, tail):
        pre = tail.next
        p = head
        while pre != tail:
            nxt = p.next
            p.next = pre
            pre = p
            p = nxt
        return tail, head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        pre = dummy

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            nxt = tail.next

            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nxt

            pre = tail
            head = tail.next

        return dummy.next
