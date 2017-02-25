Rotate List
========

Description
--------

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given `1->2->3->4->5->NULL` and `k = 2`,
return `4->5->1->2->3->NULL`.


Solution
--------

實在是很不會控制這種 `link-list`，最不混亂的做法：

*   fast 先走一遍取得總長度
*   走第二遍， fast 走到和原點距 k 時，slow 也開始一起走
*   fast 走到底時，slow 已到該切割的點
*   slow.next 為答案的 head，fast.next 跟原本的head 接上，slow 為答案的尾巴。
*   k %= length 是為了直接讓 k == length 時，可以直接輸出。

```python
class Solution(object):
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head

        slow = fast = head
        length = 1

        while fast and fast.next:
            fast = fast.next
            length += 1

        k %= length
        fast = head

        while k:
            fast = fast.next
            k -= 1

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        fast.next = head
        head = slow.next
        slow.next = None

        return head
```
