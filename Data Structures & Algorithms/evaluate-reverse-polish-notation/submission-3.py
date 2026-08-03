class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                b, a = stack.pop(), stack.pop()
                res = 0
                if tokens[i] == "+":
                    res = a + b
                elif tokens[i] == "-":
                    res = a - b
                elif tokens[i] == "*":
                    res = a * b
                elif tokens[i] == "/":
                    res = int(a / b)
                stack.append(res)

        return stack[0]