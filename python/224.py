from utils import assert_solvers


class Solution1:

    def calculate(self, s: str) -> int:
        stack = []
        def push(ch):
            if not stack or stack[-1] == '(':
                stack.append(ch)
            elif ch == ')':
                value = stack.pop()
                stack.pop() # remove '('
                push(value)
            elif isinstance(ch, int):
                op = stack.pop()
                if op == '+':
                    stack.append(stack.pop() + ch)
                elif not stack or stack[-1] == '(':
                    stack.append(-ch)
                else:
                    stack.append(stack.pop() - ch)
            else:
                stack.append(ch)

        operand = ''
        for ch in s:
            if ch.isdigit():
                operand += ch
                continue
            if operand:
                push(int(operand))
                operand = ''
            if ch != ' ':
                push(ch)

        if operand:
            push(int(operand))

        return stack[0]


class Solution2:

    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        acc = 0
        sign = 1
        for ch in s:
            if ch == ' ':
                continue
            if ch.isdigit():
                operand = operand*10 + int(ch)
                continue
            
            if ch == '+' or ch == '-':
                acc += sign*operand
            elif ch == '(':
                stack.append(sign)
                stack.append(acc)
                acc = 0
            elif ch == ')':
                acc += sign*operand
                acc = stack.pop() + stack.pop()*acc

            sign = -1 if ch == '-' else 1
            operand = 0

        acc += sign*operand

        return acc


if __name__ == '__main__':
    test_inputs = (
        (["1 + 1"], 2),
        ([" 2-1 + 2 "], 3),
        (["(1+(4+5+2)-3)+(6+8)"], 23),
        (["(-8-8)-(-7-7)"], -2),
        (["(-8- ( 7+1) - (3  - 5)) + (15 )"], 1),
        (["2234-2233"], 1),
        (["2234+2233"], 4467),
        (["2234+2233-2233-2234"], 0),
        (["1-1+1-1"], 0),
        (["(1+123+123-(-1))-(1+123+123-(-1))"], 0),
    )
    assert_solvers([Solution1().calculate, Solution2().calculate] , test_inputs)
