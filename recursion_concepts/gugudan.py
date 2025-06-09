#구구단 재귀로
def gugu(dan, num):
    print("%d * %d = %d" %(dan,num, dan*num))
    if num < 9:
        gugu(dan, num+1)

for i in range(2, 10):
    print("%d 단" %i)
    gugu(i, 1)