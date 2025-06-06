def dijkstra(graph, start):
    # TODO: 다익스트라 알고리즘 구현
    distances = {node: float('inf') for node in graph}
    visited = {node: False for node in graph}
    distances[start] = 0

    for _ in range(len(graph)):
        # 방문하지 않은 노드 중 가장 거리가 짧은 노드 찾기
        min_node = None
        min_distance = float('inf')
        for node in graph:
            if not visited[node] and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        if min_node is None:
            break  # 더 이상 방문할 수 있는 노드 없음

        visited[min_node] = True

        # 인접 노드 거리 갱신
        for neighbor, weight in graph[min_node]:
            if not visited[neighbor]:
                new_distance = distances[min_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances

graph = {
    'A': [('B', 80), ('C', 10)],
    'B': [],
    'C': [('D', 50)],
    'D': [('E', 20)],
    'E': [],
    'F': [('E', 60)]
}

start = input("시작 노드: ")
end   = input("도착 노드: ")

distances = dijkstra(graph, start)

if distances.get(end, float('inf')) == float('inf'):
    print("경로 없음")
else:
    print(f"{start} → {end} 최소 비용: {distances[end]}")
