# 기본 개념. 박스열기
def openBox(count):
    if count <= 0:
        print("박스 열기 종료")
        return
    count -= 1
    print("박스 열기")
    openBox(count)


openBox(5)