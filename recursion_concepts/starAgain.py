# 별모양
def printStar(n):
    if n > 0:
        printStar(n//2)
        print("*" * n)

printStar(20)