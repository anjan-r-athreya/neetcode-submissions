class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)

        paren = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        current_close = ''
        for i in range(n):
            if s[i] not in paren:
                stack.append(s[i])
                continue
            
            if stack and paren[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False

        if not stack:
            return True
        return False
        
        