class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        if digits == '': return []

        def combine(x, y):
            r = []
            for i in x:
                for j in mapping[y]:
                    r.append(i + j)
            return r

        return reduce(combine, list(str(digits)), [''])

if __name__ == "__main__":
    assert Solution().letterCombinations("") == []
    assert Solution().letterCombinations("2") == ["a","b","c"]
    assert Solution().letterCombinations("23") == [
        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"
    ]
