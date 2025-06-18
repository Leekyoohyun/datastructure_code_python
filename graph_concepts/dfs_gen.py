# 깊이우선탐색 일반구현
stack = []
#stack.append(val) 그냥 느낌만
data = stack.pop()

if len(stack) == 0:
    print("스택이 비었음")

visitedAry = []
visitedAry.append(0)
visitedAry.append(1)

if 1 in visitedAry:
    print("A 이미 방문")
for i in visitedAry:
    print(chr(ord('A')+i), end = ' ')


class Graph():
    def __init__(self, size):
        self.SIZE = size
        slef.graph = [[0 for _ in range(size)]for _ in range(size)]

G1 = None
stack = []
visitedAry = []

G1 = Graph(4)
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("무바햐ㅐㅇ 그래프")
for row in range(4):
    for col in range(4):
        print(G1.graph[row][col], end = ' ')
    print()

current = 0 #시작정점
stack.append(current)
visitedAry.append(current)

while(len(stack) != 0):
    next = None
    for vertex in range(4):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:
                pass
            else:
                next = vertex
                break
    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()

