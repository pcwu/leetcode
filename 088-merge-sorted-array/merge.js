/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
const merge = (nums1, m, nums2, n) => {
  while (m > 0 && n > 0) {
    nums1[m + n - 1] = (nums1[m] >= nums2[n]) ? nums1[m] : nums2[n];  
  }

};
