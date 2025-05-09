def countChar(s, target):
    # 문자열 s에서 target 문자의 개수를 세어 반환하는 재귀 함수
    if len(s) == 0:
        return 0
    else:
        # 현재 문자가 target과 같으면 1을 더하고, 아니라면 0을 더하여 재귀 호출
        count = 1 if s[0] == target else 0
        return count + countChar(s[1:], target)

text = input("문자열 입력: ")
ch = input("찾을 문자: ")
result = countChar(text, ch)
print("결과:", result)
