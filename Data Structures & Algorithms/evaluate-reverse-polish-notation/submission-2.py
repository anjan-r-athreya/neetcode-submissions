class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        operators = ["+", "-", "*", "/"]
        stack = []

        for i in range(n):
            if tokens[i] in operators:
                if tokens[i] == "+":
                    res = stack[-2] + stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif tokens[i] == "-":
                    res = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif tokens[i] == "*":
                    res = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(res)
                elif tokens[i] == "/":
                    res = int(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(res)
            else:
                currnumber = int(tokens[i])

                stack.append(currnumber)
        
        return stack[-1]