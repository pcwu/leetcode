class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result = 0

        for i in xrange(len(s)):
            if i + 1 < len(s) and d[s[i]] < d[s[i+1]]:
                result = result - d[s[i]]
            else:
                result = result + d[s[i]]
        return result
