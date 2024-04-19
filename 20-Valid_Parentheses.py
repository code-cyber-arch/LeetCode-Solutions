class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        matching_brace = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in matching_brace.values():
                stack.append(char)
            elif char in matching_brace:
                if not stack or stack.pop() != matching_brace[char]:
                    return False
            else:
                return False
        return not stack
        
