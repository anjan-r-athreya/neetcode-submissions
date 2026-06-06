class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        i = 0
        while i < len(tokens):
            currRes = 0
            if tokens[i] == "+":
                b = stack.pop()
                a = stack.pop()
                currRes = a + b
                stack.append(currRes)
            elif tokens[i] == "-":
                b = stack.pop()
                a = stack.pop()
                currRes = a - b
                stack.append(currRes)
            elif tokens[i] == "*":
                b = stack.pop()
                a = stack.pop()
                currRes = a * b
                stack.append(currRes)
            elif tokens[i] == "/":
                b = stack.pop()
                a = stack.pop()
                currRes = int(a / b)
                stack.append(currRes)
            else:
                stack.append(int(tokens[i]))
            i = i + 1
        return int(stack[0])


        # i = 0
        # while tokens[i] not in operators:
        #     stack.append(tokens[i])
        #     i += 1
        # expression = ""
        
        # for i in range(len(stack) + 1):
        #     if i == 1: expression = expression + f"{tokens[i]}

    """
    0 to 2 to 1 in to expr
    solve expr -> goes into 0, expr reset
    0 to 2 to 1 in expr
    solve expr -> goes into 0, expr reset
    """