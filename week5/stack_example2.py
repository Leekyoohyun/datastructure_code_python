#후위표기식 예제
#리스트를 이용한 stack사용함
def push(item):
    stack.append(item)

def pop():
    if len(stack) != 0:
        popData = stack.pop(-1)
        return popData

def peek():
    if len(stack)!=0:
        return stack.pop()

def compute(op, op1, op2):
    if op == "+":
        return op1+op2
    elif op == "*":
        return op1*op2
    elif op == "/":
        if op2 != 0:
            return op1/op2
        else:
            return
    elif op == "-":
        return op1-op2

def evaluate(input_expr):
    token_list = input_expr.split()

    for token in token_list:
        if token in '0123456789':
            push(int(token))
        else:
            operand2 = pop()
            operand1 = pop()
            result = compute(token, operand1, operand2)
            push(result)
    
    return pop()

stack = []
print(evaluate('7 8 + 3 2 + /'))
print(evaluate('2 3 5 * 6 4 - / +'))