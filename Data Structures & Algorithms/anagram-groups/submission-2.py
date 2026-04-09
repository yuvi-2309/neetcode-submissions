from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for str in strs:
            key = tuple(sorted(str))
            dictionary[key].append(str)

        return list(dictionary.values())
