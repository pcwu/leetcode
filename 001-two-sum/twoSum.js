/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function (nums, target) {
  const map = {};
  for (let i = 0; i <= nums.length; i += 1) {
    if (map[target - nums[i]] !== undefined) {
      return [map[target - nums[i]], i];
    }
    map[nums[i]] = i;
  }
  return [];
};
