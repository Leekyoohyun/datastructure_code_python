import random

dataAry = ['바나나맛우유', '레쓰비캔커피', '츄파춥스',
           '도시락', '삼다수', '코카콜라', '삼각김밥']

sellAry = [random.choice(dataAry) for _ in range(20)]
print('#오늘 판매된 전체 물건(중복O, 정렬X) -->', sellAry)

sellAry.sort()
print('#오늘 판매된 전체 물건(중복O, 정렬O) -->', sellAry)

sellProduct = list(set(sellAry))
print('#오늘 판매된 전체 물품 종류(중복x) -->', sellProduct)

def binSearch(arr, key):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid          # 위치 반환
        elif arr[mid] < key:     # key가 뒤쪽에 있다
            lo = mid + 1
        else:                    # key가 앞쪽에 있다
            hi = mid - 1
    return -1

countList = []
for product in sellProduct:
    count = 0
    pos = 0
    while pos != -1:
        pos = binSearch(sellAry, product)  # TODO: binSearch 호출
        if pos != -1:
            count += 1
            del sellAry[pos]
    countList.append((product, count))

print()
print("결산 결과 ==>", countList)
