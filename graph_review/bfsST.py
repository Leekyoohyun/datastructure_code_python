# 신장 트리

import collections
def bfsST(graph, start):
    visited = set([start])
    queue = collections.deque([start])
    while queue:
        v = queue.popleft()
        nbr = graph[v]-visited
        for u in nbr:
            print("("+ v+","+u+")")
            visited.add(u)
            queue.append(u)