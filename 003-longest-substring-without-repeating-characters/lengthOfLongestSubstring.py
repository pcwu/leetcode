#!/usr/bin/python
import sys


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        longest = 1
        for i in range(len(s)):
            d = {s[i]: True}
            for j in range(i+1, len(s)):
                if s[j] in d:
                    if longest < j - i:
                        longest = j - i
                    break
                elif j == len(s) - 1:
                    if j - i + 1 > longest:
                        return j - i + 1
                else:
                    d[s[j]] = True

        return longest

print Solution().lengthOfLongestSubstring(sys.argv[1])
