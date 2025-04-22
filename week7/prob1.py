# 스택/큐 정의
SIZE = 100
stack = [None] * SIZE
queue = [None] * SIZE

top = -1
front = rear = -1

# 스택 관련 함수
def isStackFull():
    return top >= SIZE - 1

def isStackEmpty():
    return top == -1

def push(data):
    global top
    if isStackFull():
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

def pop():
    global top
    if isStackEmpty():
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

# 큐 관련 함수
def isQueueFull():
    return rear == SIZE - 1

def isQueueEmpty():
    return front == rear

def enQueue(data):
    global rear
    if isQueueFull():
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global front, rear
    if isQueueEmpty():
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    # 앞으로 당기기
    for i in range(front + 1, rear + 1):
        queue[i - 1] = queue[i]
        queue[i] = None
    rear -= 1
    front = -1
    return data

# 메인 시뮬레이션
if __name__ == "__main__":
    while True:
        command = input()

        if not command:
            continue

        if command.startswith("A"):  # 기사 도착
            _, name, number = command.split()
            enQueue((name, int(number)))

        elif command == "L":  # 택배 적재
            item = deQueue()
            if item:
                push(item)

        elif command == "D":  # 택배 배송
            item = pop()
            if item:
                print(f"{item} 이번에 배송됩니다.")
            else:
                print("배송할 박스가 없습니다.")

        elif command == "P":  # 스택 상태 출력
            if isStackEmpty():
                print("스택이 비어 있습니다.")
            else:
                print(stack[top::-1][:top+1])  # 위에서 아래 순서

        elif command == "Q":  # 종료
            break

        else:
            print("알 수 없는 명령입니다.")