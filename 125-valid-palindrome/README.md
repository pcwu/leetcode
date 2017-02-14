Valid Palindrome
========



Description
--------

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
`"A man, a plan, a canal: Panama"` is a palindrome.
`"race a car"` is not a palindrome.



Solution
--------

*   2個指針，一個指最左邊，一個指最右邊
*   只要不是 alphanumeric 指針就往中間移動
*   直到兩個指針相遇，就結束
*   中間只要任一指針對，內容不相同，直接回傳 `False` 結束

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        first = 0
        last = len(s) - 1

        while last > first:
            while first <= len(s) - 1 and s[first].isalnum() is False:
                first += 1

            while last >= 0 and s[last].isalnum() is False:
                last -= 1

            if last <= first:
                return True

            if s[first].lower() != s[last].lower():
                return False

            first += 1
            last -= 1

        return True
```

別人的程式，想法相同，但稍微精簡：

```python
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True
```
