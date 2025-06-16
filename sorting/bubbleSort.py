# 버블 정렬: 첫번째 값부터 바로 앞 뒤 데이터 비교해서 정렬
#3412 -> 3142 -> 3124 -> 1324 -> 1234

import time

def bubbleSort1(ary):
    n = len(ary)
    for end in range(n-1, 0, -1): # 제일 큰 데이터 맨 뒤로 -> end -= 1
        for cur in range(0, end):
            if ary[cur] > ary[cur+1]:
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
# 근데 이러면 정렬이 되었는데도 순회를 하잖아?
# 개선
def bubbleSort2(ary):
    n = len(ary)
    for end in range(n-1, 0, -1):
        changeYN = False
        for cur in range(0, end):
            if ary[cur] > ary[cur+1]:
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                changeYN = True
        if not changeYN:
            break

wantSortAry = [3,5,4,2,7,9,10,1,6,8]
start = time.time()
bubbleSort1(wantSortAry)
end = time.time()
print(f"{end - start:.5f} sec")
print(wantSortAry)

wantSortAry = [3,5,4,2,7,9,10,1,6,8]
start = time.time()
bubbleSort2(wantSortAry)
end = time.time()
print(f"{end - start:.5f} sec")
print(wantSortAry)