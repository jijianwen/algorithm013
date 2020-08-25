# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Time complexity: O(N)
    # Space complexity: O(1)
    def getIntersect(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return slow
        return None

    def detectCycle(self, head):
        node = self.getIntersect(head)
        if not node:
            return None

        while head != node:
            head = head.next
            node = node.next

        return head
