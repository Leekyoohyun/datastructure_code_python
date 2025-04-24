#스택 활용 (괄호검사)
def isStackFull():
    global top, SIZE, stack
    if(top >= SIZE-1):
        return True
    else:
        return False

def push(data):
    global top, SIZE, stack
    if(isStackFull()):
        print("스택이 꽉참")
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, top, stack
    if(top == -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if(isStackEmpty()):
        print("스택이 비었음")
        return
    popData = stack[top]
    stack[top] = None
    top -= 1
    return popData

def checkBracket(expr):
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            open = pop()
            if open == '(' and ch == ')':
                pass
            elif open == '{' and ch == '}':
                pass
            elif open == '[' and ch == ']':
                pass
            elif open == '<' and ch == '>':
                pass
            else:
                return False
        else:
            pass
    if (isStackEmpty()):
        return True
    else:
        return False

SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == "__main__":
    exprArray = ['(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']

    for expr in exprArray:
        top = -1
        print(expr, '-->', checkBracket(expr))
