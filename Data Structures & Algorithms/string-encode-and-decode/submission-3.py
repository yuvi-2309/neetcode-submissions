class Solution:

    def encode(self, strs: List[str]) -> str:
        result_string = ""

        for string in strs:
            length = len(string)
            result_string += str(length) + '#' + string
        
        return result_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            res = s[j + 1: j + 1 + length]

            result.append(res)
            i = j + 1 + length
        
        return result


