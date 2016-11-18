class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in s:
            result = i + result
        return result
