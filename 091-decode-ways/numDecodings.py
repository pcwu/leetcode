class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)]
        dp[len(s)] = 1
        dp[len(s) - 1] = 1 if s[len(s) - 1] != '0' else 0

        for i in range(len(s) - 2, -1, -1):
            if s[i] != '0':
                if int(s[i:i + 2]) <= 26:
                    dp[i] = dp[i + 1] + dp[i + 2]
                else:
                    dp[i] = dp[i + 1]

        return dp[0]

if __name__ == '__main__':
    assert Solution().numDecodings("") == 0
    assert Solution().numDecodings("10") == 1
    assert Solution().numDecodings("100") == 0
    assert Solution().numDecodings("1010101010") == 1
    assert Solution().numDecodings("222") == 3
    assert Solution().numDecodings("332211112121") == 89
