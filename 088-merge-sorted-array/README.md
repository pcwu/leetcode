088.Merge Sorted Array
========

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

Code
--------

想法是，總共最後 nums1 這個 array 的長度會是 m + n 這麼長，所以開始把最大的數從後面往前堆。

```js
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
const merge = (nums1, m, nums2, n) => {
  while (n > 0) {
    nums1[m + n - 1] = (m === 0 || nums1[m-1] < nums2[n-1]) ? nums2[n-1] : nums1[m-1];
    if (m === 0 || nums1[m-1] < nums2[n-1]) {
      n -= 1;
    } else {
      m -=1;
    }
  }
};
```
