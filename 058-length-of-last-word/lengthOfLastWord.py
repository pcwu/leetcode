class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = s.split(" ")
        for i in xrange(len(arr)):
            if arr[len(arr)-i-1]:
                return len(arr[len(arr)-i-1])
        return 0
