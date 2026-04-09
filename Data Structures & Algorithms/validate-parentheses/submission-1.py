class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingOpeningMap = {')': '(', '}': '{', ']':'['}

        for char in s:
            if char in closingOpeningMap:
                if stack and closingOpeningMap[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False