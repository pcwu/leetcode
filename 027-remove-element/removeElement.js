/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
const removeElement = function (nums, val) {
  let last = nums.length - 1;
  let cnt = 0;
  for (let i = 0; i <= last; i += 1) {
    if (nums[i] === val) {
      while (nums[last] === val && i < last) {
        last -= 1;
      }
      if (last === i) {
        return cnt;
      }
      nums[i] = nums[last];
      last -= 1;
    }
    cnt += 1;
  }
  return cnt;
};
