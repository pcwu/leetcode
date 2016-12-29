038.Count and Say
========

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.





Code
--------


我寫的方式，用recursive

```python
class Solution(object):
    def countAndSay(self, n):
        return self.say(n, "1")

    def say(self, n, value):
        if n == 1:
            return value
        elif n > 1:
            ctr = 1
            result = ""
            while len(value) >= 2:
                if value[1] == value[0]:
                    ctr += 1
                else:
                    result = result + str(ctr) + str(value[0])
                    ctr = 1
                value = value[1:]
            result = result + str(ctr) + str(value[0])
            return self.say(n - 1, result)


```

別人的寫法，意思差不多但易讀多了：

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s
```
