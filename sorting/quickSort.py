# 퀵 정렬: 기준하나 뽑아 -> 기준보다 작은 그룹 큰 그룹 나눠 -> 반복

import time

def quickSort(ary):
    n = len(ary)
    if n<= 1:
        return ary
    pivot = ary[n//2] # 기준
    leftAry, rightAry = [], []
    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)
    
    return quickSort(leftAry)+[pivot]+quickSort(rightAry)

# 퀵정렬 일반구현
def qSort(arr, start, end):
    if end <= start:
        return
    
    low = start
    high = end
    pivot = arr[(low+high)//2]
    while low >= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low+1, high-1
    mid = low
    qSort(arr, start, mid-1)
    qSort(arr, mid, end)

wantSortAry = [3,5,4,2,7,9,10,1,6,8]
start = time.time()
ary = quickSort(wantSortAry)
end = time.time()
print(f"{end - start:.5f} sec")
print(ary)

