class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif str(x)[::-1] == str(x):
            return True
        else:
            return False
