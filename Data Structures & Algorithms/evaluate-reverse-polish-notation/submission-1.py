class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)

        for i in range(n):
            if tokens[i].lstrip("-").isnumeric():
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if tokens[i] == "+":
                    stack.append(num1 + num2)
                elif tokens[i] == "-":
                    stack.append(num1 - num2)
                elif tokens[i] == "*":
                    stack.append(num1 * num2)
                elif tokens[i] == "/":
                    stack.append(int(num1 / num2))
        return stack[-1]