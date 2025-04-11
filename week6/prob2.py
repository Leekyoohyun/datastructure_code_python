

def deQueue():
    global queue, front, rear
    if isQueueEmpty():
        print("식당 영업 종료")
        return None
    
    front += 1
    data = queue[front]
    print(data + "님이 식당에 들어감")
    queue[front] = None

    for i in range(front + 1, rear + 1):
        queue[i - 1] = queue[i]
    queue[rear] = None 
    rear -= 1
    front -= 1 

    return data


queue = ["정국", "뷔", "지민", "진", "슈가"]
front = -1
rear = len(queue) - 1

def isQueueEmpty():
    global front, rear
    if(front == rear):
        return True
    else:
        return False

# 실행
while not isQueueEmpty():
    print("대기 줄 상태: ", queue)
    deQueue()

print("대기 줄 상태: ", queue)
print("식당 영업 종료")
