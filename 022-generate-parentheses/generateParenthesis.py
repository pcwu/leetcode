class Solution(object):
    def generate(self, left, right, str, result):
        if left == 0 and right == 0:
            result.append(str)
            return
        if left > 0:
            self.generate(left - 1, right, str + "(", result)
        if right > left:
            self.generate(left, right - 1, str + ")", result)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate(n, n, "", result)
        return result



if __name__ == "__main__":
    assert Solution().generateParenthesis(0) == [""]
    assert Solution().generateParenthesis(1) == ["()"]
    assert Solution().generateParenthesis(2) == ["(())", "()()"]
    assert Solution().generateParenthesis(3) == \
        ['((()))', '(()())', '(())()', '()(())', '()()()']
