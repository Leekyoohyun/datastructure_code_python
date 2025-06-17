# 정렬되지 않은 데이터의 순차검색
def seqSearch(ary, fData):
    pos = -1
    size = len(ary)
    print("비교한 데이터 ==> ", end = ' ')
    for i in range(size):
        print(ary[i], end = ' ')
        if ary[i] == fData:
            pos = i
            break
        #실패하는 경우
        elif ary[i] > fData:
            break
    print()
    return pos

dataAry = [188, 150, 167, 162, 105, 120, 177, 50]
findData = 0

#정렬
dataAry.sort()
findData = int(input("값 입력"))
print(dataAry)

position = seqSearch(dataAry, findData)
if position == -1:
    print("없음")
else:
    print(findData,"는 ",position,"에 있음")