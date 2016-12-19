# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node = head
        if not node or not node.next:
            return None

        ctr = 1
        result = head
        while node.next:
            if ctr > n:
                result = result.next
            node = node.next
            ctr = ctr + 1
        if ctr == n:
            head = head.next
        else:
            result.next = result.next.next
        return head
