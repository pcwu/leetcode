Palindrome Number
========



## Python

這題不是拿來考python的人，所以過了就算了(PR98)

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif str(x)[::-1] == str(x):
            return True
        else:
            return False

```
