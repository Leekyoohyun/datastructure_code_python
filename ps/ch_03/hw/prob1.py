prices = [30000, 2000, 1500000]
coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    sum = 0
    prices.sort()
    coupons.sort()

    for i in range(len(prices)-1, -1, -1):
        if len(coupons) == 0:
            sum += (int)(prices[i])
            print(sum)
        else:
            sum += (int)(prices[i]*((100-coupons.pop())/100))


    return sum


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))