#원형 큐
#왜써? 그냥 큐는 오버헤드 발생하니까 끝이 없어 앞 뒤를 구부려서 연결한 느낑미라

def isQueueFull():
    global SIZE, queue, front, rear
    if((rear+1)%SIZE==front):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if(front == rear):
        return True
    else:
        return False

def enQueue(item):
    global SIZE, queue, front, rear
    if(isQueueFull()):
        print("꽉참")
        return
    rear = (rear+1)%SIZE
    queue[rear] = item

def deQueue():
    global SIZE, queue, rear, front
    if(isQueueEmpty()):
        return None
    front = (front+1)%SIZE
    data = queue[front]
    queue[front] = None
    return data

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == "__main__":
    select = input("골라라")