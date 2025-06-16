sales_data = [
    ['월','감자칩'], ['화','감자칩'], ['수','도시락'],
    ['월','생수'],   ['화','생수'],   ['금','커피우유'],
    ['토','커피우유'], ['일','커피우유'], ['화','콜라'],
    ['수','콜라'],   ['목','포카칩']
]
# ── 이진 검색 함수 ──
def binary_search(data, target):
    lo, hi = 0, len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid][1] == target:          # 상품명을 비교
            return mid
        elif data[mid][1] < target:         # target이 뒤쪽에 있음
            lo = mid + 1
        else:                               # target이 앞쪽에 있음
            hi = mid - 1
    return -1 

if __name__ == "__main__":
    # 1) 사용자 입력
    item = input("상품명을 입력하세요: ")

    # 2) 이진 검색으로 임의의 한 위치 찾기
    idx = binary_search(sales_data, item)

    if idx == -1:
        print(f"{item} 판매 기록이 없습니다.")
    else:
        # 3) 찾은 위치 기준으로 연속된 동일 상품 개수 세기
        count = 1

        # 왼쪽으로 연속 카운트
        i = idx - 1
        # TODO: i가 0 이상이고 sales_data[i][1] == item 인 동안 count 증가
        while i >= 0 and sales_data[i][1] == item:
            count += 1
            i -= 1


        # 오른쪽으로 연속 카운트
        i = idx + 1
        # TODO: i가 len(data) 미만이고 sales_data[i][1] == item 인 동안 count 증가
        while i < len(sales_data) and sales_data[i][1] == item:
            count += 1
            i += 1

        #출력
        print(f"{item} 판매 개수: {count}회")
