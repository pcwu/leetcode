Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.


```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = ptr = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                ptr = ptr.next
                l1 = l1.next
            elif l1.val > l2.val:
                ptr.next = l2
                ptr = ptr.next
                l2 = l2.next
        ptr.next = l1 or l2

        return result.next
```
