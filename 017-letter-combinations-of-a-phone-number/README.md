Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

![](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

```
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

Code
--------

本來是這樣解，

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = [
            [], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'],
            ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'], ['w', 'x', 'y', 'z']
        ]

        if digits == "":
            return []

        if len(digits) == 1:
            return mapping[int(digits)]

        def combine(x, y):
            r = []
            if type(x) is not list:
                a = mapping[int(x)]
            for i in a:
                for j in mapping[int(y)]:
                    r.append(i + j)
            return r

        return reduce(combine, list(str(digits)))
```

但覺得太醜了，參考了一下別人的，改成


```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        if digits == '': return []

        def combine(x, y):
            r = []
            for i in x:
                for j in mapping[y]:
                    r.append(i + j)
            return r

        return reduce(combine, list(str(digits)), [''])
```
