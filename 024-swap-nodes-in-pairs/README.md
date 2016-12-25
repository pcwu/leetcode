024.Swap Nodes in Pairs
========



Code
--------

想法是，遇到第奇數個，他後面還有點的話，就抽出來補在偶數後面。
所以需要記住奇數的前一個是誰(要更動他的next)，還要看偶數個有沒有next(要指定給奇數的next)

```python
class Solution(object):

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
```

別人寫類似的想法，但清爽很多：

```python
def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next
```
