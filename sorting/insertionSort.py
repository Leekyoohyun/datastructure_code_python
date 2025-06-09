# 삽입정렬
def findInsertIdx(ary, data):
    findIdx = -1
    for i in range(0, len(ary)):
        if (ary[i]>data):
            findIdx = i
            break
        if findIdx == -1:
            return len(ary) #findIdx 못찾았으면 맨 마지막에 추가해야해
        else:
            return findIdx

# 개선
def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if ary[cur-1] > ary[cur]:
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
                