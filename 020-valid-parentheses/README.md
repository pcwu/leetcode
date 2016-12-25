Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = []
        case = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for i in range(len(s)):
            if s[i] in case.values():
                result.append(s[i])
            elif result == [] or case[s[i]] != result.pop():
                return False
        return result == []

```
