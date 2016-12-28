class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in xrange(len(haystack) - len(needle)):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1
