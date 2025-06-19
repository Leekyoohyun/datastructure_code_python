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