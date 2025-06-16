# DFS 알고리즘
def dfs(graph, start, visited = set()):
    if start not in visited: # visited에 start가 기록안되어있어야. 재귀할거니까
        visited.add(start) # 일단 넣고 시작
        print(start, end = " ")
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)