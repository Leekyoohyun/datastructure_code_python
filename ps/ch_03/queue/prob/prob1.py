# 큐 문제
from collections import deque
prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    answer = []

    prices = deque(prices)

    while prices:
        current = prices.popleft()
        appendYN = False
        for idx in range(0, len(prices)):
            if(prices[idx]<current):
                answer.append(idx+1)
                appendYN = True
                break
        if(appendYN == False):
            answer.append(len(prices))
            
    return answer
    


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))