70.Climbing Stairs
========

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Code
--------

直接 recursive 一定會超時，所以把結果暫存下來：

```js
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

```
