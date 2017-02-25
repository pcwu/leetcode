class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for s in strs:
            result[tuple(sorted(s))] = result.get(tuple(sorted(s)), []) + [s]

        return sorted(result.values())

if __name__ == '__main__':
    print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
