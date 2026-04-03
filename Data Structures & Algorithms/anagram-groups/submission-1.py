from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        dictionary = defaultdict(list)

        for str in strs:
            key = tuple(sorted(str))

            dictionary[key].append(str)

        for value in dictionary.values():
            result.append(value)
        
        return result
