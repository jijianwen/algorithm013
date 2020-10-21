# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time complexity:  O(N)
    # Space complexity: O(1)
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1_nxt = l1.next
            l2_nxt = l2.next

            l1.next = l2
            l1 = l1_nxt
            l2.next = l1
            l2 = l2_nxt

    # Time complexity:  O(N)
    # Space complexity: O(N)
    def reorderList1(self, head: ListNode) -> None:
        if not head: return

        lst = list()
        node = head
        while node:
            lst.append(node)
            node = node.next

        i, j = 0, len(lst) - 1
        while i < j:
            lst[i].next = lst[j]
            i += 1
            if i == j:
                break
            lst[j].next = lst[i]
            j -= 1
        lst[i].next = None
