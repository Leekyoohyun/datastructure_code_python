# Dijkstra 최단경로 알고리즘
def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)
    dist = list(adj[start])
    path = [start] * vsize
    found = [False] * vsize
    found[start] = True
    dist[start] = 0

    for i in range(vsize):
        print("STEP%2d"%(i+1), dist)
        u = choose_vertex(dist, found)
        found[u] = True

        for w in range(vsize):
            if not found[w]:
                if dist[u]+adj[u][w] < dist[w]:
                    dist[w] = dist[u]+adj[u][w]
                    path[w] = u
    
    return path

def choose_vertex(dist, found):
    min_dist = float('inf')
    min_vertex = -1
    for i in range(len(dist)):
        if not found[i] and dist[i] < min_dist:
            min_dist = dist[i]
            min_vertex = i
    return min_vertex
