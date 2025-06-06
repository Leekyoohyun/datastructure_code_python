count = 3

def openBox():
    global count  # ← 함수 안에서 global 선언
    count -= 1
    if count == 0:
        return
    openBox()
    print("상자를 닫음")

openBox()