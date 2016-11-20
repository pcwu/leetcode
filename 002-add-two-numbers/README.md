002. Add Two Numbers
========

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

__Input:__ (2 -> 4 -> 3) + (5 -> 6 -> 4)

__Output:__ 7 -> 0 -> 8



## Code

這樣寫簡單測試以為會過了，但沒料到測資有2個linked list 長度不同的問題。

```python
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

        while l1.next != None:
            l1.next.val += (l1.val + l2.val) / 10
            l1.val = (l1.val + l2.val) % 10
            l1 = l1.next
            l2 = l2.next

        l1.val += l2.val
        if l1.val >= 10:
            l1.next = ListNode(1)
            l1.val = l1.val % 10
        return result
```

結果改成以下這樣，勝過95%的人。
想法：為了省空間，把算好的答案往l1存，如果l1比l2短的話，就將l1和l2兩個的next交換。

```python
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
                l2.val = 0
            elif l2.next is None:
                l1.next.val += (l1.val + l2.val) / 10
                l1.val = (l1.val + l2.val) % 10
                l1 = l1.next
                l2.val = 0
            else:
                l1.next.val += (l1.val + l2.val) / 10
                l1.val = (l1.val + l2.val) % 10
                l1 = l1.next
                l2 = l2.next

        return result
```
