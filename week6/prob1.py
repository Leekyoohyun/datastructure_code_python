# 전역변수 선언
SIZE = 5
queue = [None for _ in range(SIZE)]
front = -1
rear = -1

#함수 선언
def isQueueFull():
    global rear, SIZE
    if(rear == SIZE-1):
        return True
    else:
        return False
    

def isQueueEmpty():
    global front, rear
    if(front == rear):
        return True
    else:
        return False
    


def enQueue(data):
    global queue, rear
    if (isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global queue, front, rear
    if(isQueueEmpty()):
        print("큐가 비었습니다")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    
    for i in range(front + 1, rear + 1):
        queue[i - 1] = queue[i]
    queue[rear] = None 
    rear -= 1
    front -= 1 
    return data

def peek():
    global queue, front
    if(isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    return queue[front+1]
