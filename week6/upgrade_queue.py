#큐의 기능개선!
#deQueue()시 한칸씩 이동해서 빈 공간 메꿔주기
def isQueueFull():
    global SIZE, queue, rear, front
    if(rear != SIZE-1):
        return False
    if((rear == SIZE-1)and(front == -1)):
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if rear == front:
        return True
    else:
        return False

def enQueue(item):
    global SIZE, queue, rear, front
    if(isQueueFull()):
        print("큐가 꽉찼음")
        return
    rear += 1
    queue[rear] = item
    return

def deQueue():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        print("큐가 비었음")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if(isQueueEmpty()):
        return
    return queue[front+1]


