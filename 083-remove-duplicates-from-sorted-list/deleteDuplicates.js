/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
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
