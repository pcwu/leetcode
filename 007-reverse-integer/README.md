Reverse Integer
========

## Code

AC, PR32

```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result = int(str(x)[0] + str(x)[1:][::-1])
        if abs(result) > 2147483647:
            return 0
        else:
            return result

```
