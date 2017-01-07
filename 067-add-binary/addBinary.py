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
