344. Reverse String
========

一開始寫這樣，結果TLE(Time Limit Exceeded)

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in s:
            result = i + result
        return result
```

上網查了一下，發現要這樣寫才對

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
```

或者其實也可以這樣寫，先轉成List，倒序後再join接回

```python
class Solution(object):
    def reverseString(self, s):
        l = list(s)
        l.reverse()
        return ''.join(l)
```
