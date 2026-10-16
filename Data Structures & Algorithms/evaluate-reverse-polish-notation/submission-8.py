
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            # print(stack)
            if char.isdigit() or char[1:].isdigit():
                stack.append(int(char))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    stack.append(num1 + num2)
                if char == '-':
                    stack.append(num1 - num2)
                if char == '*':
                    stack.append(num1 * num2)
                if char == '/':
                    stack.append(int(num1 / num2))
        return stack.pop()
                

            


        