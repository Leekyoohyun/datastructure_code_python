def solution(numbers, target):
    answer = 0
    leaves = [0]

    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent+num)
            tmp.append(parent-num)
        leaves = tmp
    
    for t in leaves:
        if t == target:
            answer += 1
    return answer

numb = [1, 1, 1, 1, 1]
print(solution(numb, 3))