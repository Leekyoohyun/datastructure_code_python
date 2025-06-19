# 버블정렬
import time


def BubbleSort(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        for cur in range(0, end):
            if ary[cur] > ary[cur+1]:
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
    return ary


def BubbleSort2(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        changeYN = False
        for cur in range(0, end):
            if ary[cur] > ary[cur+1]:
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                changeYN = True
        if changeYN == False:
            break
    
    return ary


testAry = [1,25,6621,243,214,141,536,61412]


print(testAry)
start = time.time()
print(BubbleSort2(testAry))
end = time.time()
print(start- end)