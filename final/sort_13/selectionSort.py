# 선택정렬
import time

def findMinIdx(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[i] < ary[minIdx]:
            minIdx = i

    return minIdx

def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if ary[k] < ary[minIdx]:
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
    
    return ary

testAry = [1,25,6621,243,214,141,536,61412]


print(testAry)
start = time.time()
print(selectionSort(testAry))
end = time.time()
print(start- end)

