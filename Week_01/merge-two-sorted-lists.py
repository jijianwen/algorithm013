# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        pre_node = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                pre_node.next = l1
                l1 = l1.next
            else:
                pre_node.next = l2
                l2 = l2.next
            pre_node = pre_node.next
        
        pre_node.next = l1 if l1 is not None else l2

        return dummy.next
