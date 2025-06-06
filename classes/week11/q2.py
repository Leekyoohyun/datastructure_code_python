def hasPath(graph, start, end, visited):
    if start == end:
        return True
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            if hasPath(graph, neighbor, end, visited):
                return True
    return False



road_map = {
    'Seoul': ['Incheon', 'Daejeon'],
    'Incheon': ['Seoul', 'Daejeon'],
    'Daejeon': ['Seoul', 'Incheon', 'Daegu'],
    'Daegu': ['Daejeon', 'Busan'],
    'Busan': ['Daegu'],
    'Jeju': []  # 고립된 도시
}

start = input("출발 도시: ")
end = input("도착 도시: ")
visited = set()

# 결과 출력
if hasPath(road_map, start, end, visited):
    print("길 있음")
else:
    print("길 없음")
