from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for i in range(len(s)):
            char  = s[i]
            if (char in ['(','{','[']): # if char == ( or char == {
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if (char == ')'):
                    if not (stack.pop() == '('):
                        return False
                if (char == ']'):
                    if not (stack.pop() == '['):
                        return False
                if (char == '}'):
                    if not (stack.pop() == '{'):
                        return False
        return len(stack) == 0

        