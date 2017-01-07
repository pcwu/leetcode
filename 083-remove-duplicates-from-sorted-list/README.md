083.Remove Duplicates from Sorted List
========

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Code
--------

如果 ptr 的值跟 ptr.next 的值相同，就直接將指標往後跳，跳到 ptr 和 ptr.next 的值不相同。

```js
const deleteDuplicates = (head) => {
  if (!head) {
    return head;
  }
  ptr = head;
  while (ptr.next) {
    if (ptr.val === ptr.next.val) {
      ptr.next = ptr.next.next;
    } else {
      ptr = ptr.next;
    }
  }
  return head;
};
```
