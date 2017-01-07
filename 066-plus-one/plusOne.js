/**
 * @param {number[]} digits
 * @return {number[]}
 */
const plusOne = (digits) => {
  let carry = 1;
  for (let i = 1; i <= digits.length; i += 1) {
    digits[digits.length - i] += carry;

    if (digits[digits.length - i] > 9){
      digits[digits.length - i] -= 10;
      carry = 1;
    } else {
      carry = 0;
    }
  }
  if (carry === 1){
    return [1, ...digits];
  }
  return digits;

};
