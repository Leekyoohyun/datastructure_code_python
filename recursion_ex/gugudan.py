# 구구단
def gugu(dan, num):
    print("%d * %d = %d" % (dan, num, dan*num))
    if num < 9:
        gugu(dan, num+1)

gugu(2, 1)