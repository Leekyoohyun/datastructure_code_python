class Node:
    def __init__(self):
        self.name = None
        self.email = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    
    print(f"['{current.name}', '{current.email}']", end=' ')
    while current.link != None:
        current = current.link
        print(f"['{current.name}', '{current.email}']", end=' ')
    print()

def addNode(name, email):
    global memory, head, current, pre
    node = Node()
    node.name = name
    node.email = email
    if head == None:  # 첫 번째 노드
        head = node
    else:
        current = head
        while current.link != None:
            current = current.link
        current.link = node
    memory.append(node)

# 전역 변수 선언
memory = []
head, current, pre = None, None, None

# 메인 코드
if __name__ == "__main__":
    while True:
        name = input("이름 --> ")
        if name == "":
            break
        email = input("이메일 --> ")
        addNode(name, email)
        printNodes(head)

