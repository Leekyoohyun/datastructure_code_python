def fact(num):
    if num <= 1:
        print("1반환")
        return 1
    fact_result = num * fact(num-1)

    return fact_result

print(fact(5))