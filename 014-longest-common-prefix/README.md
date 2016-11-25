014. Longest Common Prefix
========



## Code

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        result = strs[0]
        for i in xrange(len(strs)):
            j = 0
            while j < len(result) and j < len(strs[i]) and result[j] == strs[i][j]:
                    j = j + 1

            result = result[0:j]

            if len(result) == 0:
                return ""
        return result

```
