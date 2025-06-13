# BFS 알고리즘

import collections

def bfs(graph, start):
    #큐 사용할거임
    visited = set([start])
    queue = collections.deque([start])
    while queue: # 큐가 있으면 
        vertex = queue.popleft()
        print(vertex, " ")
        nbr = graph[vertex]-visited
        for v in nbr:
            visited.add(v)
            queue.append(v)