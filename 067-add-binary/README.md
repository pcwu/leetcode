067.Add Binary
========

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".


Code
--------

簡單先變成list然後翻轉過來，加完之後再翻轉回來join回string。

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l = []
        s = []
        carry = 0

        if len(a) > len(b):
            l = list(a[::-1])
            s = list(b[::-1])
        else:
            l = list(b[::-1])
            s = list(a[::-1])

        for i in xrange(len(s)):
            l[i] = str(int(s[i]) + int(l[i]) + carry)
            if int(l[i]) >= 2:
                carry = 1
                l[i] = str(int(l[i]) % 2)
            else:
                carry = 0

        i = len(s)
        while carry == 1:
            if len(l) == i:
                l.append("1")
                carry = 0
            elif l[i] == "1":
                l[i] = "0"
                carry = 1
            else:
                l[i] = "1"
                carry = 0
            i += 1

        return "".join(l[::-1])

```

網路上看到別人是用recursive：

```python
#add two binary from back to front, I think it is very self explained, when 1+1 we need a carry.
   class Solution:
        def addBinary(self, a, b):
            if len(a)==0: return b
            if len(b)==0: return a
            if a[-1] == '1' and b[-1] == '1':
                return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
            if a[-1] == '0' and b[-1] == '0':
                return self.addBinary(a[0:-1],b[0:-1])+'0'
            else:
                return self.addBinary(a[0:-1],b[0:-1])+'1'
```
