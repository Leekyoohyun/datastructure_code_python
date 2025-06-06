import random

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


memory = []
root = None
dataAry = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sellAry = [random.choice(dataAry) for _ in range(20)]
print("오늘 판매된 물건(중복O) -->", sellAry)


node = TreeNode()
node.data = sellAry[0]
root = node
memory.append(node)

for name in sellAry[1:]:
    node = TreeNode()
    node.data = name
    current = root

    while True:
        # 1) 이미 있는 값이면 삽입하지 않고 종료
        if name == current.data:
            break

        # 2) name이 작으면 왼쪽 서브트리에 삽입
        elif name < current.data:
            if current.left is None:
                current.left = node
                memory.append(node)
                break
            else:
                current = current.left

        # 3) name이 크면 오른쪽 서브트리에 삽입
        else:  # name > current.data
            if current.right is None:
                current.right = node
                memory.append(node)
                break
            else:
                current = current.right

print("이진 탐색 트리 구성 완료!")

def preorder(node):
    if node is None:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)

print("오늘 판매된 종류(중복X) -->", end=' ')
preorder(root)
