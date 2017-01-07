/**
 * @param {number} n
 * @return {number}
 */
const climbStairs = (n) => {
  const data = { 1: 1, 2: 2 };

  const countStairs = (i) => {
    if (data[i]) {
      return data[i];
    }
    data[i - 1] = countStairs(i - 1);
    data[i - 2] = countStairs(i - 2);
    return data[i - 1] + data[i - 2];
  };
  return countStairs(n);
};
