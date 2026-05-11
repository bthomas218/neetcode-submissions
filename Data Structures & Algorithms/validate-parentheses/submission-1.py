class Solution:
    def isValid(self, s: str) -> bool:
        closings = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stack = []

        for char in s:
            if char in closings:
                if not stack:
                    return False
                opening = stack.pop()
                if opening != closings[char]:
                    return False
                continue
            stack.append(char)
        
        return len(stack) == 0