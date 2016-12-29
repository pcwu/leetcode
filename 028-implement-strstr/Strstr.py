class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0

        for i in xrange(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1
