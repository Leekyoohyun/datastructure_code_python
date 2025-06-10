# factorial
def factorial(num):
    if num <= 1:
        return
    print("%d * %d" % (num, num-1))
    retVal = factorial(num-1)

    print("%d * %d!(=%d) 반환" % (num, num-1, retVal))
    return num * retVal

print(factorial(5))