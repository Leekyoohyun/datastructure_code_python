# 삽입정렬
def findInsertionIdx(ary, data):
    findIdx = -1
    for i in range(0, len(ary)):
        if ary[i] > data:
            findIdx = i
            break
    if findIdx == -1:
        return len(ary)
    else:
        return findIdx
    

def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if ary[cur] < ary[cur-1]:
                ary[cur], ary[cur-1] = ary[cur-1], ary[cur]
    return ary

