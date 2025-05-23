class Graph():
    def __init__(self, n):
        self.SIZE = n
        self.graph = [[0]*n for _ in range(n)]

def printGraph(g):
    # 헤더
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(cityAry[v], end=' ')
    print()
    # 각 행
    for i in range(g.SIZE):
        print(cityAry[i], end=' ')
        for j in range(g.SIZE):
            print(f"{g.graph[i][j]:2d}", end=' ')
        print()
    print()

# Union-Find
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra != rb:
        parent[rb] = ra
        return True
    return False


#— 전역 변수 및 원본 그래프 세팅 —#
cityAry = ['서울','뉴욕','런던','북경','방콕','파리']
서울,뉴욕,런던,북경,방콕,파리 = 0,1,2,3,4,5
N = 6

G1 = Graph(N)
# (양방향)
edges = [
    (80, 서울, 뉴욕), (10, 서울, 북경),
    (40, 뉴욕, 북경), (70, 뉴욕, 방콕),
    (30, 런던, 방콕), (60, 런던, 파리),
    (50, 북경, 방콕),
    (20, 방콕, 파리)
]
for w,u,v in edges:
    G1.graph[u][v] = G1.graph[v][u] = w

print('## 해저 케이블 연결을 위한 전체 연결도 ##')
printGraph(G1)


#— 최대 신장 트리 구성 (내림차순 Kruskal + Union-Find) —#
# 1) 간선 후보 추출 (i<j 로 중복 제거)
edgeAry = []
for i in range(N):
    for j in range(i+1, N):
        w = G1.graph[i][j]
        if w:
            edgeAry.append((w,i,j))

# 2) 속도 내림차순 정렬
edgeAry.sort(reverse=True, key=lambda x: x[0])

# 3) Kruskal
parent = list(range(N))
G2 = Graph(N)
count = 0
for w,u,v in edgeAry:
    if count == N-1:
        break
    if union(parent, u, v):
        G2.graph[u][v] = G2.graph[v][u] = w
        count += 1

print('## 가장 효율적인 해저 케이블 연결도 (그림과 동일) ##')
printGraph(G2)
