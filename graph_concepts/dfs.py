# dfs
stack = []
visitedAry = []

current = 0 #시작 정점
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
        

