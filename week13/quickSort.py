#Quick sort 기준 하나 뽑아서 그룹 나눠 -> 다시 각 그룹으로 정렬
def qSort(arr, start, end):
    if start >= end:
        return
    
    low = start
    high = end

    pivot = arr[(low+high)//2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = high, low
    
    mid = low
    qSort(arr, start, mid -1)
    qSort(arr, mid, end)

def quickSort(ary):
    qSort(ary, 0, len(ary)-1)