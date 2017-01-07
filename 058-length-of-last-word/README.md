058.Length of Last Word
=========
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.


Code
--------

本來是這樣寫：

不過會出問題，當input是"a "，時會輸出0，但應該要是1

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split(" ")[-1])

```

最後改成這樣：

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = s.split(" ")
        for i in xrange(len(arr)):
            if arr[len(arr)-i-1]:
                return len(arr[len(arr)-i-1])
        return 0
```
