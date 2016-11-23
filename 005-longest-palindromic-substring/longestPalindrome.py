#!/usr/bin/python
import sys


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = 0
        ans = ""
        if len(s) == 0:
            return 0
        for i in xrange(len(s)):
            l = 1
            tmp = s[i]
            if i + 1 < len(s) and s[i] == s[i+1]:
                l = 2
                j = 1
                while i - j >= 0 and i + 1 + j < len(s):
                    if s[i - j] == s[i + 1 + j]:
                        l = l + 2
                    else:
                        break
                    j = j + 1
                tmp = s[i-j+1:i+j+1]
            if l > result:
                result = l
                ans = tmp
            if i + 2 < len(s) and s[i] == s[i+2]:
                l = 3
                j = 1
                while i - j >= 0 and i + 2 + j < len(s):
                    if s[i - j] == s[i + 2 + j]:
                        l = l + 2
                    else:
                        break
                    j = j + 1
                tmp = s[i-j+1:i+j+2]
            if l > result:
                result = l
                ans = tmp
        if result == 0:
            return s[-1]
        else:
            return ans

print Solution().longestPalindrome(sys.argv[1])
