Rotate Image
========


Description
--------

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?


Solution
--------

想破頭想不出來要怎麼做，偷看了一下別人的做法：

1.  先上下對稱翻轉，也就是 `[i, y] <=> [n-i, y]` 交換
2.  再以`左上-右下`為對稱軸翻轉，也就是 `[x, y] <=> [y, x]` 交換

```
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
```
逆時鐘的話，則變成是

1.  先左右對稱翻轉，也就是 `[x, i] <=> [x, n-i]` 交換
2.  再以`左上-右下`為對稱軸翻轉，也就是 `[x, y] <=> [y, x]` 交換

```
/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
```


Reference
--------

*   [https://discuss.leetcode.com/topic/15295/seven-short-solutions-1-to-7-lines](https://discuss.leetcode.com/topic/15295/seven-short-solutions-1-to-7-lines)

*   [https://discuss.leetcode.com/topic/6796/a-common-method-to-rotate-the-image](https://discuss.leetcode.com/topic/6796/a-common-method-to-rotate-the-image)
