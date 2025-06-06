class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print(' ', end='')
    for v in range(g.SIZE):
        print("%9s" % storeAry[v][0], end=' ')
    print()
    for row in range(g.SIZE):
        print("%9s" % storeAry[row][0], end=' ')
        for col in range(g.SIZE):
            print("%8d" % g.graph[row][col], end=' ')
        print()
    print()

# 편의점 정보
storeAry = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4

# 그래프 구성
gSize = 5
G1 = Graph(gSize)

G1.graph[GS25][CU] = 1; G1.graph[GS25][Seven11] = 1
G1.graph[CU][GS25] = 1; G1.graph[CU][Seven11] = 1; G1.graph[CU][MiniStop] = 1
G1.graph[Seven11][GS25] = 1; G1.graph[Seven11][CU] = 1; G1.graph[Seven11][MiniStop] = 1
G1.graph[MiniStop][Seven11] = 1; G1.graph[MiniStop][CU] = 1; G1.graph[MiniStop][Emart24] = 1
G1.graph[Emart24][MiniStop] = 1

print('## 편의점 그래프 ##')
printGraph(G1)

# === TODO: DFS 탐색 구현  ===
visited = [False] * gSize
maxStore = -1
maxChip = -1

def DFS(v):
    global maxStore, maxChip
    visited[v] = True
    # 현재 편의점의 허니버터칩 개수 비교
    if storeAry[v][1] > maxChip:
        maxChip = storeAry[v][1]
        maxStore = v
    for i in range(gSize):
        if G1.graph[v][i] == 1 and not visited[i]:
            DFS(i)

# 탐색 시작
DFS(GS25)

# 결과 출력
print('허니버터칩 최대 보유 편의점(개수) -->', storeAry[maxStore][0], '(', storeAry[maxStore][1], ')')
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print(' ', end='')
    for v in range(g.SIZE):
        print("%9s" % storeAry[v][0], end=' ')
    print()
    for row in range(g.SIZE):
        print("%9s" % storeAry[row][0], end=' ')
        for col in range(g.SIZE):
            print("%8d" % g.graph[row][col], end=' ')
        print()
    print()

# 편의점 정보
storeAry = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4

# 그래프 구성
gSize = 5
G1 = Graph(gSize)

G1.graph[GS25][CU] = 1; G1.graph[GS25][Seven11] = 1
G1.graph[CU][GS25] = 1; G1.graph[CU][Seven11] = 1; G1.graph[CU][MiniStop] = 1
G1.graph[Seven11][GS25] = 1; G1.graph[Seven11][CU] = 1; G1.graph[Seven11][MiniStop] = 1
G1.graph[MiniStop][Seven11] = 1; G1.graph[MiniStop][CU] = 1; G1.graph[MiniStop][Emart24] = 1
G1.graph[Emart24][MiniStop] = 1

print('## 편의점 그래프 ##')
printGraph(G1)

# === TODO: DFS 탐색 구현  ===
visited = [False] * gSize
maxStore = -1
maxChip = -1

def DFS(v):
    global maxStore, maxChip
    visited[v] = True
    # 현재 편의점의 허니버터칩 개수 비교
    if storeAry[v][1] > maxChip:
        maxChip = storeAry[v][1]
        maxStore = v
    for i in range(gSize):
        if G1.graph[v][i] == 1 and not visited[i]:
            DFS(i)

# 탐색 시작
DFS(GS25)

# 결과 출력
print('허니버터칩 최대 보유 편의점(개수) -->', storeAry[maxStore][0], '(', storeAry[maxStore][1], ')')
