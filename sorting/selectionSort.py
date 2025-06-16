# 선택정렬
def findMinIdx(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[i] < ary[minIdx]:
            minIdx = i
    return minIdx

# 선택정렬 개선
def selectionSort(ary):
    n = len(ary)
    for i in range(n-1):
        minIdx = i
        for k in range(i+1, n):
            if(ary[minIdx] > ary[k]):
                minIdx = k
        tmp = ary[minIdx]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
    
    return ary