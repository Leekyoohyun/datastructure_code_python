def dfs(graph, start, visited = set()):
    if start not in visited:
        visited.add(start)
        print(start, end = ' ')
        nbr = graph[start] - visited
        print(nbr)
        for v in nbr:
            dfs(graph, v, visited)

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

dfs(graph, 'A')
