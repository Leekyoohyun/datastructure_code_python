# 스택 정의
SIZE = 100
stack = [None] * SIZE
top = -1

# 스택 함수
def isStackFull():
    return top >= SIZE - 1

def isStackEmpty():
    return top == -1

def push(data):
    global top
    if isStackFull():
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

def pop():
    global top
    if isStackEmpty():
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    if isStackEmpty():
        return None
    return stack[top]

# 메인 코드 부분
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 --> ").strip()

    while select.lower() != 'x':  # 대소문자 구분 없이 처리
        if select.lower() == 'i':  # 삽입
            data = input("입력할 데이터 ==> ").strip()
            push(data)
            print("스택 상태 : ", stack[:top + 1])
        elif select.lower() == 'e':  # 추출
            data = pop()
            print("추출된 데이터 ==> ", data)
            print("스택 상태 ==> ", stack[:top + 1])
        elif select.lower() == 'v':  # 확인
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("스택 상태 ==> ", stack[:top + 1])
        else:
            print("정해진 입력만 하세요 (I, E, V, X)")

        select = input("\n삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 --> ").strip()

    print("프로그램 종료!")
