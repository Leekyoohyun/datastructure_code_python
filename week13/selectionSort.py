# 선택정렬: 가장 작은값 뽑기 반복
def findMin(ary):
    min = 0
    for i in range(1, len(ary)):
        if(ary[i]<ary[min]):
            min = i
    return min

# 선택정렬 개선
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        min = i
        for k in range(i+1, n-1):
            if ary[min] > ary[k]:
                min = k
        ary[i], ary[min] = ary[min], ary[i]
    
    return ary