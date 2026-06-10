class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetopen = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in closetopen:
                if stack and closetopen[c]==stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return True if not stack else False
        