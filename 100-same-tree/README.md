100.Same Tree
========

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Code
--------

想法很簡單，都是空的話，回傳 true，然後只有一個是空的話 回傳 false，然後都不是空的時，直不同就回傳 false，最後就比子樹。

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
const isSameTree = (p, q) => {
  if (p === null && q === null) {
    return true;
  }
  if (p === null || q === null) {
    return false;
  }
  if (p.val != q.val) {
    return false;
  }

  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);

};
```

但看了一下別人的方法，可以整理成：

如果p和q都存在的話：看p和q值是否相等，同時子樹們是否相等。

如果p和q沒有都存在的話，直接看p等不等於q

```js
const isSameTree = (p, q) => {
  if (p && q) {
    return p.val === q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
  }
  return p === q;
};
```
