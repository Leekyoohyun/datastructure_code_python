# 이진 탐색 트리
name = "findname"

class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

node = TreeNode()
node.data = name
current = root

while True:
    if name < current.data:
        if current.left == None:
            current.left = node
            break
        current = current.left
    else:
        if current.right == None:
            current.right = node
            break
        current = current.right

# 이진트리 검색
findName = "찾는이름"

current = root
while True:
    if findName == current:
        print("찾")
        break
    elif findName < current:
        if current.left == None:
            print("없")
            break
        current = current.left
    else:
        if current.right == None:
            print("없")
            break
        current = current.right

# 이진트리 삭제
deleteName = "삭제할이름"
current = root
parent = None

while True:
    if deleteName == current.data:
        if current.left == None and current.right == None:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del(current)  # current 지우기 전 밑작업 느낌
        elif current.left != None and current.right == None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.right
            del(current)
        elif current.left == None and current.right != None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.right
            del(current)

        print("삭제 끝")
        break
    elif deleteName < current.data:
        if current.left == None:
            print("없")
            break
        parent = current
        current = current.left
    
    else:
        if current.right == None:
            print("없")
            break
        parent = current
        current = current.right
