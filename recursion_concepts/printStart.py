# 별 출력하기 (재귀)
def printStar(n):
    if n > 0:
        printStar(n-1)
        print("*"*n)

printStar(5)