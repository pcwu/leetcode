# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = result = ListNode(0)
        pre.next = result.next = head

        while head and head.next:
            odd = head
            even = head.next
            pre.next = even
            odd.next = even.next
            even.next = odd
            head = head.next
            pre = pre.next.next

        return result.next
