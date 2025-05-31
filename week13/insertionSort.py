#삽입정렬: 기존 데ㅣ터 중 자신의 위치 찾아서 삽입하기
def findInsertIdx(ary, data):
    findIdx = -1
    for i in range(0, len(ary)):
        if(ary[i]>data):
            findIdx = i
            break
        if findIdx == -1:
            return len(ary)
        else:
            return findIdx
        
#개선 
def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if(ary[cur-1]>ary[cur]):
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]

    return ary