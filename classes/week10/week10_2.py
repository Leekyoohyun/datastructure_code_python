def reversePrint(string):
    # 재귀를 사용하여 문자열을 거꾸로 출력
    if len(string) == 0:
        return
    else:
        # 문자열의 마지막 문자를 먼저 출력하고, 나머지 문자열로 재귀 호출
        print(string[-1], end='')
        reversePrint(string[:-1])

text = input("문자열 입력: ")
reversePrint(text)
