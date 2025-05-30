# ── 함수 선언 부분 ──
def scoreSort(ary):
    """
    ary: [['이름', 점수], ...] 형태의 리스트
    insertion sort 알고리즘으로 ary를 점수 오름차순 정렬 후 반환
    """
    for i in range(1, len(ary)):
        key = ary[i]
        j = i - 1
        while j >= 0 and key[1] < ary[j][1]:
            ary[j + 1] = ary[j]
            j -= 1
        ary[j + 1] = key
    return ary

# ── 전역 변수 선언 부분 ──
scoreAry = [
    ['선미', 88],
    ['초아', 99],
    ['화사', 71],
    ['영탁', 78],
    ['영웅', 67],
    ['민호', 92]
]

# ── 메인 코드 부분 ──
if __name__ == "__main__":
    print('정렬 전 -->', scoreAry)
    scoreAry = scoreSort(scoreAry)
    print('정렬 후 -->', scoreAry)

    print('## 성적별 조 편성표 ##')
    n = len(scoreAry)
    for i in range(n // 2):
        print(f"{scoreAry[i][0]} : {scoreAry[n - 1 - i][0]}")
