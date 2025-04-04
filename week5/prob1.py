SIZE = 5
stack = [None] * SIZE
top = -1

def isStackFull():
    return top >= SIZE - 1

def isStackEmpty():
    return top == -1

def push(data):
    global top
    if isStackFull():
        print("스택이 가득 찼습니다.")
        return
    top += 1
    stack[top] = data
    print(f"push: {data}")

def pop():
    global top
    if isStackEmpty():
        print("스택이 비어 있습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    print(f"pop: {data}")
    return data
