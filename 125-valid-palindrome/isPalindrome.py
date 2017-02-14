class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        first = 0
        last = len(s) - 1

        while last > first:
            while first <= len(s) - 1 and s[first].isalnum() is False:
                first += 1

            while last >= 0 and s[last].isalnum() is False:
                last -= 1

            if last <= first:
                return True

            if s[first].lower() != s[last].lower():
                return False

            first += 1
            last -= 1

        return True

if __name__ == "__main__":
    assert Solution().isPalindrome("") is True
    assert Solution().isPalindrome(".") is True
    assert Solution().isPalindrome("..") is True
    assert Solution().isPalindrome("a") is True
    assert Solution().isPalindrome("Aa") is True
    assert Solution().isPalindrome("a0") is False
    assert Solution().isPalindrome("aba") is True
    assert Solution().isPalindrome("xy...yx") is True
    assert Solution().isPalindrome("xy..yx") is True
    assert Solution().isPalindrome("xyxy") is False
