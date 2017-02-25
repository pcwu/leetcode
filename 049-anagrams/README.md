Group Anagrams
========

Description
--------

Given an array of strings, group anagrams together.

For example, given: `["eat", "tea", "tan", "ate", "nat", "bat"]`,

Return:

```
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

Solution
--------

這樣會超時：

```python
class Solution(object):
    def groupAnagrams(self, strs):
        result = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in result.keys():
                result[key].append(s)
            else:
                result[key] = [s]

        return sorted(result.values())
```
改成這樣：

```python
class Solution(object):
    def groupAnagrams(self, strs):
        result = {}
        for s in strs:
            result[tuple(sorted(s))] = result.get(tuple(sorted(s)), []) + [s]

        return sorted(result.values())
```
