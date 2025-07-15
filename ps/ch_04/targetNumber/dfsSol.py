answer = 0
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer

def dfs(numbers, target, cur, idx):
    global answer
    if(len(numbers) == idx):
        if target == cur:
            answer += 1
        return
    
    dfs(numbers, target, cur+numbers[idx], idx+1)
    dfs(numbers, target, cur-numbers[idx], idx+1)
    