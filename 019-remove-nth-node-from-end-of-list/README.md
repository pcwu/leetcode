Given a linked list, remove the nth node from the end of list and return its head.

For example,

```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

Note:
Given n will always be valid.
Try to do this in one pass.


# Code

```python
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
```
