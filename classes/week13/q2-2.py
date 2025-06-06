import random
import time

# ── 선택 정렬 ──
def selectionSort(arr):
    # TODO: 선택 정렬 구현
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# ── 삽입 정렬 ──
def insertionSort(arr):
    # TODO: 삽입 정렬 구현
   for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# ── 버블 정렬 ──
def bubbleSort(arr):
    # TODO: 버블 정렬 구현
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# ── 퀵 정렬 보조 함수 ──
def _qsort(arr, lo, hi):
    if lo >= hi:
        return
    pivot = arr[(lo + hi)//2]
    i, j = lo, hi
    # TODO: partition 로직 구현
    # TODO: 재귀 호출
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
    _qsort(arr, lo, j)
    _qsort(arr, i, hi)

def quickSort(arr):
    """
    퀵 정렬: _qsort 호출 후 arr 반환
    """
    _qsort(arr, 0, len(arr)-1)
    return arr

# ── 메인 코드 ──
if __name__ == "__main__":
    sizes = [1000, 10000, 12000, 15000]
    for n in sizes:
        data = [random.randint(10000, 99999) for _ in range(n)]
        funcs = [
            ("선택 정렬",   selectionSort),
            ("삽입 정렬",   insertionSort),
            ("버블 정렬",   bubbleSort),
            ("퀵 정렬",     quickSort),
        ]

        print(f"## 데이터 수: {n}개")
        for name, fn in funcs:
            arr = data[:]            
            start = time.time()
            result = fn(arr) or arr  
            elapsed = time.time() - start
            print(f"\t{name} --> {elapsed:.3f}초")
        print()
