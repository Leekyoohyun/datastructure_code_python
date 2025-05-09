## 함수 선언 부분 ##
def notation(base, n):
    # 재귀를 사용하여 진법 변환
    if n == 0:
        return
    else:
        notation(base, n // base)  # 다음 자리수 계산
        print(numberChar[n % base], end='')  # 현재 자리수 출력
    
## 전역 변수 선언 부분 ##
numberChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numberChar += ['A', 'B', 'C', 'D', 'E', 'F']

## 메인 코드 부분 ##
number = int(input('10진수 입력 --> '))

print('\n2진수 : ', end=' ')
notation(2, number)

print('\n8진수 : ', end=' ')
notation(8, number)

print('\n16진수 : ', end=' ')
notation(16, number)
