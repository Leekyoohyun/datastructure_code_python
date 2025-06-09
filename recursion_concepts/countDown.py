def countDown(countNum):
    if countNum == 0:
        print("발사")
    else:
        print(countNum)
        countDown(countNum-1)

        # 이거 순서 바꾸면 스택느낌. 생각해봐
        # countDown(countNum-1)
        # print(countNum)

countDown(5)