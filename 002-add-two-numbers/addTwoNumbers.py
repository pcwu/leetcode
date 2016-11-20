# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = l1

        while True:
            if l1.next is None and l2.next is None:
                l1.val += l2.val
                if l1.val >= 10:
                    l1.next = ListNode(1)
                    l1.val = l1.val % 10
                break
            elif l1.next is None:
                l1.next = l2.next
                l2.next = None
                l1.next.val += (l1.val + l2.val) / 10
                l1.val = (l1.val + l2.val) % 10
                l1 = l1.next
            elif l2.next is None:
                l1.next.val += l1.val / 10
                l1.val = l1.val % 10
                l1 = l1.next
            else:
                l1.next.val += (l1.val + l2.val) / 10
                l1.val = (l1.val + l2.val) % 10
                l1 = l1.next
                l2 = l2.next

        return result
