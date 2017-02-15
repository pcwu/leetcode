Linked List Cycle
========

Description
--------

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?


Solution
--------


*   想法是用2個指針，快指針一次走2步，慢指針一次走一步。2個指針如果重疊了就是結束了。
*   不太懂為什麼不能用一個指針，然後跟 `head` 比就好了？
*   這題因為沒辦法測，做不太下去，於是錯了幾次直接參考別人答案。

```python
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```
