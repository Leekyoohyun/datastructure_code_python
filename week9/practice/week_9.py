class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

nodeA.left = nodeB
nodeA.right = nodeC
nodeB.left = nodeD
nodeB.right = nodeE
nodeC.right = nodeF
nodeF.left = nodeG

def printLeafNodes(node):
    # TODO
    if node is None:
        return
    # 왼쪽/오른쪽 둘 다 없으면 리프 노드
    if node.left is None and node.right is None:
        print(node.data, end=' ')
        return
    # 자식이 있으면 재귀 탐색
    printLeafNodes(node.left)
    printLeafNodes(node.right)
    

print("리프 노드: ", end='')
printLeafNodes(nodeA)
print() #%가 끝에 찍혀서 추가
